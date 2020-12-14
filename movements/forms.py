
from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length



class MovementForm(FlaskForm):
    id = IntegerField('id')
    fecha = DateField('Fecha', validators=[DataRequired()])
    concepto = StringField('Concepto', validators=[DataRequired(), Length(min=10, message="El concepto debe tener más de 10 caracteres")])
    cantidad = FloatField('Cantidad', validators=[DataRequired()])

    submit = SubmitField('Aceptar')