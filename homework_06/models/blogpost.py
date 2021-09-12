from datetime import datetime

from models.database import db
from sqlalchemy import func 
from sqlalchemy.orm import relationship


class Blogpost(db.Model):
    __tablename__ = 'blogposts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    date_posted = db.Column(
        db.DateTime,
        default=datetime.utcnow(),
        server_default=func.now(),
    )
    content = db.Column(db.Text)
    author_id = db.Column(
        db.Integer, db.ForeignKey("authors.id"), unique=True
    )

    author = db.relationship("Author", back_populates="posts")
