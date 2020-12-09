from movements import app
from flask import render_template, request
import csv

@app.route("/")
def listaIngresos():
    fIngresos = open("movements/data/basededatos.csv", "r")
    csvReader = csv.reader(fIngresos, delimiter = ",", quotechar = '"')
    ingresos = list(csvReader)
    sumador = 0
    for ingreso in ingresos:
        sumador += float(ingreso[2])
    
    print(ingresos)
    
    return render_template("movementList.html", datos=ingresos, total=sumador)

@app.route("/crealta", methods=["GET", "POST"])
def nuevoIngreso ():
    if request.method == "POST":
        print(request.form)
        
    
    return render_template("alta.html")