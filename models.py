from app import db
from manage import db,app

class Listing(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer)
    date_start = db.Column(db.DateTime())
    date_end = db.Column(db.DateTime())
    category = db.Column(db.String())
    location = db.Column(db.String())
    price = db.Column(db.Integer)
    description = db.Column(db.String())
    skills = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)