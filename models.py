from app import db

class Listing(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, nullable=True)
    date_start = db.Column(db.DateTime(), nullable=True)
    date_end = db.Column(db.DateTime(), nullable=True)
    category = db.Column(db.String(), nullable=True)
    location = db.Column(db.String(), nullable=True)
    price = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(), nullable=True)
    skills = db.Column(db.String(), nullable=True)

    def __init__(self, business_id, date_start, date_end, category, location, price, description, skills):
        self.business_id = business_id
        self.date_start = date_start
        self.date_end = date_end
        self.category = category
        self.location = location
        self.price = price
        self.description = description
        self.skills = skills



class Worker(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64) , nullable=True)
    email = db.Column(db.String(120), index=True, nullable=True)
    phone_number = db.Column(db.String(), nullable=True)
    experiences = db.Column(db.String(), nullable=True)
    skills = db.Column(db.String(), nullable=True)
    location = db.Column(db.String(), )
    profile_img = db.Column(db.String())
    bio = db.Column(db.String(), nullable=True)
    links = db.Column(db.String(), nullable=True)
    certifications = db.Column(db.String(), nullable=True)


    def __init__(self, name, email, phone_number, experiences, skills, location, profile_img, bio, links, certifications):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.experiences = experiences
        self.skills = skills
        self.location = location
        self.profile_img = profile_img
        self.bio = bio
        self.links = links
        self.certifications = certifications