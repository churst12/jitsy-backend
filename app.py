from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/jitsy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

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

class Test(db.Model):

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

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/display')
def view_listings():
	from models import Listing
	listings = Listing.query.all()
	return listings

if __name__ == '__main__':
    app.run(debug=True)