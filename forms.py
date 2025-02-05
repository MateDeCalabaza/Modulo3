#Usamos la libreria de WTFlask para realizar el formulario (la descargamos previamente con pip)
from flask_wtf import FlaskForm
#Aquí importamos, campodetexto, validadoresdedatos, y el boton submit
from wtforms import StringField, validators, SubmitField
#Aquí de los validadores importamos el dato obligatorio
from wtforms.validators import DataRequired

class MiFormulario(FlaskForm):
    name = StringField(label='Nombre', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired()])
    message = StringField(label='Mensaje')
    submit = SubmitField(label="Enviar")