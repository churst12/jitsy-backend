
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jitsy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

import models

# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    username = request.json['nickname']
    email = request.json['email']
    
    new_user = models.User(username, email)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)

@app.route('/')
def home():
    return "jitsy"




if __name__ == '__main__':
    app.run(debug=True)