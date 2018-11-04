from app import db
from sqlalchemy.dialects.postgresql import JSON


class Listing(db.Model):

    id = db.Column(db.Integer)
    business_id = db.Column(db.Integer)
    date_start = db.Column(db.DateTime())
    date_end = db.Column(db.DateTime())
    category = db.Column(db.String())
    location = db.Column(db.String())
    price = db.Column(db.Integer)
    description = db.Column(db.String())
    skills = db.Column(JSON)

    def __repr__(self):
        return '<id {}>'.format(self.id)