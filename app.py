from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jitsy.db'
app.congfig['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User, Listing


@app.route('/')
def home():
    return "fuck you"


if __name__ == '__main__':
    app.run(debug=True)