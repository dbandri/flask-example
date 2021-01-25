from wtforms import Form
from wtforms import StringField
from wtforms.fields.html5 import EmailField

class contactForm(Form):
    fullname = StringField('fullname')
    phone = EmailField('email')
    email = StringField('phone')