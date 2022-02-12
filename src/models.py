from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    #favorite_planets = db.relationship("FavoritePlanet", backref="planet_faver")
    #favorite_characters = db.relationship("FavoriteCharacter", backref="char_faver")
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "active": self.is_active, 
            # do not serialize the password, its a security breach
        }