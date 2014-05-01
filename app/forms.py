from flask_wtf import Form
from wtforms import TextField, HiddenField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, EqualTo


class ApplicationForm(Form):
    squirrel            = TextField("")

    name_msg            = "Please provide your full name. This helps us find you faster!"
    name                = TextField("Your Full Name", [Required(name_msg)])

    email_msg           = "Your email is required."
    email               = EmailField('Your Email', [Required(email_msg)])

    email_confirm_req   = "Please confirm your email address."
    email_confirm_msg   = "Check to be sure your email matches."
    email_confirm       = EmailField('Confirm Your Email', 
                            [
                                Required(email_confirm_req),
                                EqualTo('email', message=email_confirm_msg)
                            ])

    phone_message       = "We need your phone number, please."
    phone               = TextField("Your Phone Number", [Required(phone_message)])

    submit              = SubmitField("Send Us Your Application!")
