from flask_wtf import Form
from wtforms import TextField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, EqualTo


class ApplicationForm(Form):
    name_msg            = "We need to know who you are."
    name                = TextField("Your name", [Required(name_msg)])

    email_msg           = "Your email is required."
    email               = EmailField('Your Email', [Required(email_msg)])

    confirm_email_req   = "Please confirm your email address."
    confirm_email_msg   = "Check to be sure your email matches."
    confirm_email       = EmailField('Confirm Your Email', 
                            [
                                Required(confirm_email_req),
                                EqualTo('confirm_email', message=confirm_email_msg)
                            ])

    name_msg            = "Please provide your full name. This helps us find you faster!"
    name                = TextField("Full name", [Required(name_msg)])

    phone_message       = "We need your phone number, please."
    phone               = TextField("Your phone number", [Required(phone_message)])
