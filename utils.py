from faker import Faker
from models import Lead
from database import db

fake = Faker()

def generate_fake_leads(n):
    for _ in range(n):
        lead = Lead(
            name=fake.name(),
            latitude=fake.latitude(),
            longitude=fake.longitude(),
            temperature=fake.random_int(min=35, max=40),
            interest=fake.word(),
            email=fake.unique.email(),  #desafio 1., desafio 2.
            telefone=fake.phone_number()  #desafio 1., desafio 2.
        )
        db.session.add(lead)
    db.session.commit()
