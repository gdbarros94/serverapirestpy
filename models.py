from database import db

class Lead(db.Model):
    __tablename__ = 'leads'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    interest = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False) #desafio 1.
    telefone = db.Column(db.String(15), nullable=False) #desafio 1.

    def __init__(self, name, latitude, longitude, temperature, interest, email, telefone): #desafio 1.
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.temperature = temperature
        self.interest = interest
        self.email = email #desafio 1.
        self.telefone = telefone #desafio 1.

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'temperature': self.temperature,
            'interest': self.interest,
            'email': self.email, #desafio 1.
            'telefone': self.telefone #desafio 1.
        }
