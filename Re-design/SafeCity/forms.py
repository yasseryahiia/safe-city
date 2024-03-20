from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , BooleanField



class RegisterForm(FlaskForm):
    username = StringField(label='Username')  
    password = PasswordField(label='Password') 
    location = StringField(label='Location')  
    #camera_id = BooleanField(label='CameraID')
    submit = SubmitField(label='Sign up')