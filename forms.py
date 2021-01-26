from wtforms import Form
from wtforms import StringField
from wtforms.fields.html5 import EmailField
from wtforms.fields.html5 import TelField

class contactForm(Form):
    fullname = StringField('Nombre')
    email = EmailField('Correo')
    phone = TelField('Telefono')