from app import db
from datetime import datetime

# create models for database tables


class Task(db.Model):
    """Task model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """Return a string representation of the task."""
        return f"Task('{self.title}', '{self.description}', '{self.status}')"


class User(db.Model):
    """User model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """Return a string representation of the user."""
        return f"User('{self.username}', '{self.email}')"