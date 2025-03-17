from app import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    format = db.Column(db.String(50), nullable=False)
    tags = db.Column(db.String(255), nullable=True)
    upload_date = db.Column(db.DateTime, default=db.func.now())

class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=True)
