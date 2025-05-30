from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from backend.database import db

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plaid_access_token = db.Column(db.String(255), nullable=True)
    plaid_item_id = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100))
    official_name = db.Column(db.String(255))
    type = db.Column(db.String(50))
    subtype = db.Column(db.String(50))
    mask = db.Column(db.String(10))
    current_balance = db.Column(db.Float)
    available_balance = db.Column(db.Float)
    institution_name = db.Column(db.String(255))
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    name = db.Column(db.String(255))
    amount = db.Column(db.Float)
    category = db.Column(db.String(100))
    date = db.Column(db.Date)
    pending = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
