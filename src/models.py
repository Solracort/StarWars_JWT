from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # is_active = db.Column(db.Boolean(), nullable=True)
    tabla_Favorites = db.relationship('Favorites', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            
            # do not serialize the password, its a security breach
        }    

class Personaje(db.Model):
    idpersonaje = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return '<Personaje %r>' % self.idpersonaje
    
    def serialize(self):
        return {
            "id": self.idpersonaje,
            "name": self.name,
            # do not serialize the password, its a security breach
        }    
    

    
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return '<Vehicle %r>' % self.id

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iduser= db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    # idpersonaje = db.Column(db.Integer, db.ForeignKey("Personaje.idpersonaje"))
    # idplanet    = db.Column(db.Integer, db.ForeignKey("Planet.idplanet"))
    # idvehicle   = db.Column(db.Integer, db.ForeignKey("Vehicle.idvehicle"))
    
    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            # "usuario": self.iduser,
            
            # do not serialize the password, its a security breach
        }    
    
    
    

    