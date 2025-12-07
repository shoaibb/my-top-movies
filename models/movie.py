from db import db

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)

    users = db.relationship('UserMovies', backref='movie', lazy=True)