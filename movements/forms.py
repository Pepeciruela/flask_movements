
from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField, FloatField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length


def must_contain_one_digit(form, field):
    for c in '0123456789':
        if c in field.data:
            return None
    raise ValidationError('Debe contener al menos un número')


class MovementForm(FlaskForm):
    fecha = DateField('Fecha', validators=[DataRequired()])
    concepto = StringField('Concepto', validators=[DataRequired(), Length(min=10, message="El concepto debe tener más de 10 caracteres"), must_contain_one_digit])
    cantidad = FloatField('Cantidad', validators=[DataRequired()])

    submit = SubmitField('Aceptar')