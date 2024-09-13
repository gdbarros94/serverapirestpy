from faker import Faker
from models import Lead
from database import db

fake = Faker()

def generate_leads(n):
    for _ in range(n):
        lead = Lead(
            name=fake.name(),
            latitude=fake.latitude(),
            longitude=fake.longitude(),
            temperature=fake.random_int(min=35, max=40),
            interest=fake.word(),
            email=fake.email(), #desafio 1.
            telefone=fake.phone_number() #desafio 1.
        )
        db.session.add(lead)
    db.session.commit()

