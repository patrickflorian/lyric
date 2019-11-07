from .. import db
import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Genre(db.Model):
    """Genre model to store related genres details"""
    __tablename__ = "genre"

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    registered_on = db.Column(db.DateTime, nullable=False)

class Lyric(db.Model):
    """Lyric model to store related lyrics details"""
    __tablename__ = "lyric"

    id = db.Column(db.String(100), primary_key=True)
    public_id = db.Column(db.String(100), unique=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    audio = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    genre_id = db.Column(db.String(100),ForeignKey("genre.id"))
    genre = relationship("Genre")