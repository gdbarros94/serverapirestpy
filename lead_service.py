import re  #desafio 2.
from models import Lead

class LeadService:
    def __init__(self, db):
        self.db = db

    def validate_email(self, email):  #desafio 2.
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  #desafio 2.
        return re.match(pattern, email) is not None  #desafio 2.

    def validate_telefone(self, telefone):  #desafio 2.
        pattern = r'^\(\d{2}\) \d{4,5}-\d{4}$'  #desafio 2.
        return re.match(pattern, telefone) is not None  #desafio 2.

    def create_lead(self, name, latitude, longitude, temperature, interest, email, telefone):  #desafio 1., desafio 2.
        if not self.validate_email(email):  #desafio 2.
            raise ValueError("E-mail inválido!")  #desafio 2.
        if not self.validate_telefone(telefone):  #desafio 2.
            raise ValueError("Telefone inválido!")  #desafio 2.
        if Lead.query.filter_by(email=email).first():  #desafio 2.
            raise ValueError("E-mail já cadastrado!")  #desafio 2.

        lead = Lead(name=name, latitude=latitude, longitude=longitude, temperature=temperature, interest=interest, email=email, telefone=telefone)  #desafio 1., desafio 2.
        self.db.session.add(lead)
        self.db.session.commit()

    def update_lead(self, lead_id, name, latitude, longitude, temperature, interest, email, telefone):  #desafio 1., desafio 2.
        lead = self.get_lead_by_id(lead_id)

        if not self.validate_email(email):  #desafio 2.
            raise ValueError("E-mail inválido!")  #desafio 2.
        if not self.validate_telefone(telefone):  #desafio 2.
            raise ValueError("Telefone inválido!")  #desafio 2.
        if Lead.query.filter_by(email=email).first() and lead.email != email:  #desafio 2.
            raise ValueError("E-mail já cadastrado!")  #desafio 2.

        lead.name = name
        lead.latitude = latitude
        lead.longitude = longitude
        lead.temperature = temperature
        lead.interest = interest
        lead.email = email  #desafio 1., desafio 2.
        lead.telefone = telefone  #desafio 1., desafio 2.
        self.db.session.commit()
    def get_all_leads(self):
          return Lead.query.all()
    def get_lead_by_id(self, lead_id):
          return Lead.query.get_or_404(lead_id)
    def update_lead(self, lead_id, name, latitude, longitude, temperature, interest, email, telefone): #desafio 1.
        lead = self.get_lead_by_id(lead_id)
        lead.name = name
        lead.latitude = latitude
        lead.longitude = longitude
        lead.temperature = temperature
        lead.interest = interest
        lead.email = email #desafio 1.
        lead.telefone = telefone #desafio 1.
        self.db.session.commit()
    def delete_lead(self, lead_id):
        lead = self.get_lead_by_id(lead_id)
        self.db.session.delete(lead)
        self.db.session.commit()
