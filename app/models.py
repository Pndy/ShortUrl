from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from random import choice
from string import ascii_lowercase, ascii_uppercase, digits


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<{} - {}>'.format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(_id):
    return User.query.get(int(_id))


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    var_id = db.Column(db.String(6), unique=True)
    url = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    click_counter = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Url {}>'.format(self.url)

    def gen_var_id(self):
        # Generate random 6 letter/number long variable
        # Might need to check for duplicated at some point
        self.var_id = ''.join(choice(ascii_uppercase + ascii_lowercase + digits) for i in range(6))
