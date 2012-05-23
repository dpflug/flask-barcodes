from wtforms import Form, TextField
from wtforms.validators import Length, Email
from wtforms.validators import Required
class RegistrationForm(Form):
    fullname = TextField(
            'Full Name',
            [Required(), Length(min=2, max=200)]
        )
    email = TextField('Email Address', [Required(), Email()])
