
from datetime import datetime

from models.database import db
from sqlalchemy import func
from sqlalchemy.orm import relationship


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    posts = relationship("Blogpost", back_populates="author")

