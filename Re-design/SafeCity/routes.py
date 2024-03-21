from SafeCity import app
from flask import render_template , redirect , url_for
from SafeCity import db
from SafeCity.models import User , Snapshots

#when added a table in db u should add his import here too
from SafeCity.models import Snapshots
from SafeCity.forms import RegisterForm


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



@app.route("/signup" , methods=['POST','GET'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(Username=form.username.data,
                              password_hash=form.password.data,
                              location=form.location.data
                              )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('signup'))

    return render_template("signup.html",form=form)

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
