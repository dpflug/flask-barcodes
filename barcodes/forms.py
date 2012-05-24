from flaskext.wtf import Form, TextField, Length, Email, Required
from flaskext.wtf.html5 import EmailField


class RegistrationForm(Form):
    fullname = TextField(
            'Full Name',
            [Required(), Length(min=2, max=200)]
        )
    email = EmailField('Email Address', [Required(), Email()])
