
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow

from flask_sqlalchemy import SQLAlchemy

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



worker_schema = WorkerSchema()
workers_schema = WorkerSchema(many=True)


# endpoint to create new user
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

    return "201 Created"
@app.route('/worker', methods=["GET"])
def get_workers():
    all_workers = models.Worker.query.all()
    result = workers_schema.dump(all_workers)
    return jsonify(result.data)
@app.route('/')
def home():
    return "jitsy"




if __name__ == '__main__':
    app.run(debug=True)