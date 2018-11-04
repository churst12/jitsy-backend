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
    job_title = db.Column(db.String(), nullable=True)
    company_name = db.Column(db.String(), nullable=True)
    start_time = db.Column(db.String(), nullable=True)
    end_time = db.Column(db.String(), nullable=True)
    date = db.Column(db.String(), nullable=True)
    status = db.Column(db.String(), nullable=True)
    wage = db.Column(db.Integer, nullable=True)
    photo = db.Column(db.String(), nullable=True)
    location = db.Column(db.String(), nullable=True)
    description = db.Column(db.String(), nullable=True)
    skills = db.Column(db.String(), nullable=True)
    applied = db.Column(db.Boolean(), nullable=True)

    def __init__(self, job_title, company_name, start_time, end_time, date, status, wage, photo, location, description, skills, applied):
        self.job_title = job_title
        self.company_name = company_name
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
        self.status = status
        self.wage = wage
        self.photo = photo
        self.location = location
        self.description = description
        self.skills = skills
        self.applied = applied



class Worker(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64) , nullable=True)
    email = db.Column(db.String(120), index=True, nullable=True)
    phone_number = db.Column(db.String(), nullable=True)
    experiences = db.Column(db.String(), nullable=True)
    skills = db.Column(db.String(), nullable=True)
    location = db.Column(db.String(), nullable=True)
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