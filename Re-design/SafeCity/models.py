from SafeCity import db
from SafeCity import func # for time


class User(db.Model):
    Username = db.Column(db.String(length=50), nullable=False, primary_key=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    location = db.Column(db.String(length=60), nullable=False)

    camera_id = db.Column(db.Integer()) #unique=True or False ?

    #relationship between User and Snapshots
    alerts = db.relationship('Snapshots', backref='owned_user', lazy=True)

class Snapshots(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Detection_img_ref = db.Column(db.String(length=100), nullable=False)
    Detection_type = db.Column(db.String(length=30), nullable=False)
    Loc = db.Column(db.String(length=100), nullable=False)    
    Time = db.Column(db.DateTime(timezone=True),server_default=func.now())

    #relationship between User and Snapshots
    Alert_sentTo = db.Column(db.String(length=50), db.ForeignKey('user.Username'), nullable=False)

    

    def __repr__(self):
        return f'Snapshots {self.Loc}'
