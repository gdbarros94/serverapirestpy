import re
from models import Lead

class LeadService:
    def __init__(self, db):
        self.db = db

    def get_leads(self, page, per_page):
        return Lead.query.paginate(page=page, per_page=per_page, error_out=False)  # Paginação na listagem de leads

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def validate_telefone(self, telefone):
        pattern = r'^\(\d{2}\) \d{4,5}-\d{4}$'
        return re.match(pattern, telefone) is not None

    def create_lead(self, name, latitude, longitude, temperature, interest, email, telefone):
        if not self.validate_email(email):
            raise ValueError("E-mail inválido!")
        if not self.validate_telefone(telefone):
            raise ValueError("Telefone inválido!")
        if Lead.query.filter_by(email=email).first():
            raise ValueError("E-mail já cadastrado!")

        lead = Lead(name=name, latitude=latitude, longitude=longitude, temperature=temperature, interest=interest, email=email, telefone=telefone)
        self.db.session.add(lead)
        self.db.session.commit()

    def update_lead(self, lead_id, name, latitude, longitude, temperature, interest, email, telefone):
        lead = self.get_lead_by_id(lead_id)

        if not self.validate_email(email):
            raise ValueError("E-mail inválido!")
        if not self.validate_telefone(telefone):
            raise ValueError("Telefone inválido!")
        if Lead.query.filter_by(email=email).first() and lead.email != email:
            raise ValueError("E-mail já cadastrado!")

        lead.name = name
        lead.latitude = latitude
        lead.longitude = longitude
        lead.temperature = temperature
        lead.interest = interest
        lead.email = email
        lead.telefone = telefone
        self.db.session.commit()

    def get_lead_by_id(self, lead_id):
        return Lead.query.get_or_404(lead_id)

    def delete_lead(self, lead_id):
        lead = self.get_lead_by_id(lead_id)
        self.db.session.delete(lead)
        self.db.session.commit()
