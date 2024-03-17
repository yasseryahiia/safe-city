from SafeCity import db
from SafeCity import func # for time

class Snapshots(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Detection_img_ref = db.Column(db.String(length=100), nullable=False)
    Detection_type = db.Column(db.String(length=30), nullable=False)
    Loc = db.Column(db.String(length=100), nullable=False)
    Alert_sentTo = db.Column(db.String(80), unique=True, nullable=False)
    Time = db.Column(db.DateTime(timezone=True),server_default=func.now())

    def __repr__(self):
        return f'Snapshots {self.Loc}'
