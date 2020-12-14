from movements import app
from flask import render_template, request, url_for, redirect
import csv
import sqlite3

BDFILE = "movements/data/basededatos.db"

def consulta(query, params):
    conn = sqlite3.connect(BDFILE) # crear conexión
    c = conn.cursor() # crear cursor
    
    c.execute(query, params) #ejecutar los parámetros
    filas = fetchall()
    con.commit()
    conn.close()
    if len(filas) == 0:
        return None
    
    columnNames = []
    for columnNames in c.description: #se añaden los nombres en la lista
        columnNames.append(columnNames[0])
    
    listaDeDiccionarios = []
    
    for fila in filas:
        d = {}
        for ix, columnName in enumerate(columnNames):
            d[columnName] = fila[ix]
            listaDeDiccionarios.append(d)
    
    if len (listaDeDiccionarios) == 1:
        return listaDeDiccionarios [0]
    else:
        return listaDeDiccionarios

@app.route('/')
def listaIngresos():
    ingresos = consulta("SELECT fecha, concepto, cantidad, id FROM movimientos;") or [] # ejecutar lo seleccionado

    total = 0
    for ingreso in ingresos:
        total += float(ingreso["cantidad"])
        
    conn.close()

    return render_template("movementsList.html",datos=ingresos, total=total)

@app.route('/creaalta', methods=['GET', 'POST'])
def nuevoIngreso():
    if request.method == 'POST':
        
        conn = sqlite3.connect(BDFILE)
        c = conn.cursor()
    
        c.execute("INSERT INTO movimientos (cantidad, concepto, fecha) VALUES (?,?,?);", 
                  (
                      float(request.form.get("cantidad")), 
                      request.form.get("concepto"), 
                      request.form.get("fecha")
                      ))
        
        
        return redirect(url_for("listaingresos"))

    return render_template("alta.html")

@app.route("/modifica/<id>", methods=["GET", "POST"])
def modificaingreso(id):
    conn = sqlite3.connect(BDFILE)
    c = conn.cursor()
    
    if request.method == "GET":
        registro = consulta("SELECT fecha, concepto, cantidad, id FROM movimientos where id = ?", (id,))
        registro = c.fetchone() #recuperas el registro
    
        conn.close()
    
        return render_template("modifica.html", registro=registro)
    else:
        c.execute("UPDATE movimientos SET fecha = ?, concepto = ?, cantidad = ? WHERE id =?", 
                  (request.form.get("fecha"),
                   request.form.get ("concepto"),
                   float(request.form.get("cantidad")),
                   id
                   )
                  )
        conn.commit() #ratificar el cambio
        conn.close () #cierra conexión con la base de datos
        
        return redirect(url_for("listaIngresos")) # devuelve la respuesta al navegador y le dice que lo siguiente es la petición a 
        