
from . import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash 

class User(db.Document, UserMixin):
    name = db.StringField(required=False, max_length=80, index=True)
    email = db.EmailField(unique=True, required=True, sparse=True, max_length=80, index=True)
    phone = db.StringField(unique=True, required=True)
    password_hash = db.StringField(required=False, index=True)
    manager = db.BooleanField(default=False, unique=False)

    def __repr__(self):
        return f"Username: {self.username} id: {self.id}"

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
