from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    species = db.Column(db.String(30), nullable=False)
    photo_url = db.Column(db.String, default='https://www.thesprucepets.com/thmb/cqchehWYVdsOdOAjEas1emSsZVo=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/BulldogPuppy-6e41129e2f8d44afba459d1c900d0ff3.jpg')
    age = db.Column(db.Integer)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean, nullable=False, default=True)
    