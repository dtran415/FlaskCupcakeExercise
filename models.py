"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_CUPCAKE_IMG = 'https://curric.springboard.com/software-engineering-career-track/default/exercises/flask-cupcakes/_images/cupcake.jpg'

def connect_db(app):
    
    db.app = app
    app.app_context().push()
    db.init_app(app)

class Cupcake(db.Model):
    
    __tablename__ = "cupcakes"
    
    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_CUPCAKE_IMG)
    
    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }