from flask import Flask, render_template, Response, request, session
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SafeCity.db'
db = SQLAlchemy(app)
app.app_context().push()

class Snapshots(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Detection_img_ref = db.Column(db.String(length=100), nullable=False)
    Detection_type = db.Column(db.String(length=30), nullable=False)
    Loc = db.Column(db.String(length=100), nullable=False)
    Alert_sentTo = db.Column(db.String(80), unique=True, nullable=False)
    Time = db.Column(db.DateTime(timezone=True),server_default=func.now())

    def __repr__(self):
        return f'Snapshots {self.Loc}'

from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename
import os
import cv2
#from YOLO_Video import video_detection , video_detection2
import numpy as np


# app.config['SECRET_KEY'] = 'muhammadmoin'
# app.config['UPLOAD_FOLDER'] = r'C:\Users\yassi\Desktop\web app\crowd videos'
#
# class UploadFileForm(FlaskForm):
#     file = FileField("File", validators=[InputRequired()])
#     submit = SubmitField("Run")

# def generate_frames_web(path_x):
#     yolo_output = video_detection(path_x)
#     for detection_ in yolo_output:
#         ref, buffer = cv2.imencode('.jpg', detection_)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')




@app.route("/signin")
@app.route("/")
def login():
    return render_template("signin.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/alerts")
def snapshot():
    snaps=Snapshots.query.all()
    return render_template("alerts.html",snaps = snaps )



@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/livestream")
def live():
    return render_template("livestream.html")

@app.route("/analytics")

def analysis():
    return render_template("analytics.html")

# @app.route('/', methods=['GET', 'POST'])
# def default():
#     session.clear()
#     return render_template('index.html')

# @app.route('/FrontPage', methods=['GET', 'POST'])
# def front():
#     form = UploadFileForm()
#     if form.validate_on_submit():
#         file = form.file.data
#         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
#                                secure_filename(file.filename)))
#         session['video_path'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
#                                              secure_filename(file.filename))
#     return render_template('videoprojectnew.html', form=form)
#
# @app.route('/webapp')
# def webapp():
#     return Response(generate_frames_web(path_x=0), mimetype='multipart/x-mixed-replace; boundary=frame')
#


if __name__ == "__main__":
    app.run(debug=True)