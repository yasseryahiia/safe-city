from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField



class RegisterForm(FlaskForm):
    username = StringField(label='Username')  
    password1 = PasswordField(label='Password') 
    location = StringField(label='Location:')  
    submit = SubmitField(label='Sign up')