from app import db

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(), nullable=True)
    name = db.Column(db.String(), nullable=True)
    bio = db.Column(db.String(), nullable=True)
    cover_img = db.Column(db.String(), nullable=True)
    profile_img = db.Column(db.String(), nullable=True)
    other_img = db.Column(db.String(), nullable=True)
    category = db.Column(db.String(), nullable=True)
    email = db.Column(db.String(), nullable=True)
    phone_number = db.Column(db.String(), nullable=True)

    def __init__(self, location, name, bio, cover_img,profile_img, other_img, category, email, phone_number):
        self.location = location
        self.name = name
        self.bio = bio
        self.cover_img = cover_img
        self.profile_img = profile_img
        self.other_img = other_img
        self.category = category
        self.email = email
        self.phone_number = phone_number

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, nullable=True)
    worker_id = db.Column(db.Integer, nullable=True)
    date = db.Column(db.DateTime(), nullable=True)
    content = db.Column(db.String(), nullable=True)
    score = db.Column(db.Integer, nullable=True)
    listing_id = db.Column(db.Integer, nullable=True)
    reviewer_type = db.Column(db.String(), nullable=True)

    def __init__(self, business_id, worker_id, date, content, score, listing_id, reviewer_type):
        self.business_id = business_id
        self.worker_id = worker_id
        self.date = date
        self.content = content
        self.score = score
        self.listing_id = listing_id
        self.reviewer_type = reviewer_type

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