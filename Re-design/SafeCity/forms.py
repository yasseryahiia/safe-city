from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , BooleanField,ValidationError
from wtforms.validators import Length , DataRequired
from SafeCity.models import User



class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(Username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

            

    username = StringField(label='Username' , validators=[Length(min=3,max=20),DataRequired()])  
    password = PasswordField(label='Password' , validators=[Length(max=20),DataRequired()]) 
    location = StringField(label='Location', validators=[DataRequired()])  
    #camera_id = BooleanField(label='CameraID',validators=[DataRequired()])
    submit = SubmitField(label='Sign up')
