
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
import nexmo
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jitsy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

import models

class WorkerSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name', 'email', 'phone_number', 'experiences','skills','location','profile_img','bio','links','certifications')

class ListingSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('job_title','company_name', 'start_time', 'end_time', 'date', 'status', 'wage', 'photo', 'location','description','skills','applied')

class BusinessSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('location','name', 'bio','cover_img','profile_img','other_img','category','email', 'phone_number')

class ReviewSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('business_id', 'worker_id', 'date', 'content', 'score', 'listing_id', 'reviewer_type')



worker_schema = WorkerSchema()
workers_schema = WorkerSchema(many=True)

listing_schema = ListingSchema()
listings_schema = ListingSchema(many=True)

business_schema = BusinessSchema()
businesses_schema = BusinessSchema(many=True)

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

######
#WORKER
@app.route("/worker", methods=["POST"])
def add_worker():
    email = request.json['email']
    name = request.json['name']
    phone_number = request.json['phone_number']
    experiences = request.json['experiences']
    skills = request.json['skills']
    location = request.json['location']
    profile_img = request.json['profile_img']
    bio = request.json['bio']
    links = request.json['links']
    certifications = request.json['certifications']
    
    new_worker = models.Worker(name, email,phone_number, experiences,skills,location,profile_img,bio,links,certifications)

    db.session.add(new_worker)
    db.session.commit()

    return "201 Created Worker"
@app.route('/worker', methods=["GET"])
def get_workers():
    all_workers = models.Worker.query.all()
    result = workers_schema.dump(all_workers)
    return jsonify(result.data)
#######

#######
#LISTING
@app.route("/listing", methods=["POST"])
def add_listing():
    job_title = request.json['job_title']
    company_name = request.json['company_name']
    start_time = request.json['start_time']
    end_time = request.json['end_time']
    date = request.json['date']
    status = request.json['status']
    wage = request.json['wage']
    photo = request.json['photo']
    location = request.json['location']
    description = request.json['description']
    skills = request.json['skills']
    applied = request.json['applied']
    
    new_listing = models.Listing(job_title, company_name, start_time, end_time, date, status, wage, photo, location, description, skills, applied)

    db.session.add(new_listing)
    db.session.commit()

    client = nexmo.Client(key='78ca5126', secret='6hnzpSo1P0U6vPvt')
    client.send_message({'from': '17402240276', 'to': '14087310723', 'text': 'New Listing near you in {0} for the wage of: ${1}'.format(location,wage)})

    return "201 Created Listing"

@app.route('/listing', methods=["GET"])
def get_listings():
    all_listings = models.Listing.query.all()
    result = listings_schema.dump(all_listings)
    return jsonify(result.data)
##########

#BUSINESS
@app.route("/business", methods=["POST"])
def add_business():
    location = request.json['location']
    name = request.json['name']
    bio = request.json['bio']
    cover_img = request.json['cover_img']
    profile_img = request.json['profile_img']
    other_img = request.json['other_img']
    category = request.json['category']
    email = request.json['email']
    phone_number = request.json['phone_number']
    
    new_business = models.Business(location,name, bio,cover_img,profile_img,other_img,category,email, phone_number)

    db.session.add(new_business)
    db.session.commit()

    return "201 Created Business"

@app.route('/business', methods=["GET"])
def get_businesses():
    all_businesses = models.Business.query.all()
    result = businesses_schema.dump(all_businesses)
    return jsonify(result.data)
##########

#REVIEWS
@app.route("/review", methods=["POST"])
def add_review():
    business_id = request.json['business_id']
    worker_id = request.json['worker_id']
    date = datetime.strptime(request.json['date'], '%b %d %Y %I:%M%p')
    content = request.json['content']
    score = request.json['score']
    listing_id = request.json['listing_id']
    reviewer_type = request.json['reviewer_type']
    
    new_review = models.Review(business_id, worker_id, date, content, score, listing_id, reviewer_type)

    db.session.add(new_review)
    db.session.commit()

    return "201 Created Review"

@app.route('/review', methods=["GET"])
def get_reviews():
    all_reviews = models.Review.query.all()
    result = reviews_schema.dump(all_reviews)
    return jsonify(result.data)
##########

@app.route("/nexmo",methods=["GET"])
def get_nexmo():
    client = nexmo.Client(key='78ca5126', secret='6hnzpSo1P0U6vPvt')
    client.send_message({'from': '17402240276', 'to': '14087310723', 'text': 'New Listing near you in Mountain View, CA! "Lifeguard" for $15/hr '})
    return "Success"

@app.route('/')
def home():
    return "jitsy"




if __name__ == '__main__':
    app.run(debug=True)