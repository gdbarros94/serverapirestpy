import re
from models import Lead

class LeadService:
    def __init__(self, db):
        self.db = db

    def get_leads(self, page, per_page, search_name=None):  # Desafio 4: Adicionado o parâmetro search_name
        query = Lead.query
        if search_name:  # Desafio 4: Filtrando por nome, se fornecido
            query = query.filter(Lead.name.ilike(f"%{search_name}%"))  # Desafio 4: Implementação da busca por nome
        return query.paginate(page=page, per_page=per_page, error_out=False)  # Desafio 4: Usando a query filtrada ou padrão

    def validate_email(self, email):  # Desafio 2.
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  # Desafio 2.
        return re.match(pattern, email) is not None  # Desafio 2.

    def validate_telefone(self, telefone):  # Desafio 2.
        pattern = r'^\(\d{2}\) \d{4,5}-\d{4}$'  # Desafio 2.
        return re.match(pattern, telefone) is not None  # Desafio 2.

    def create_lead(self, name, latitude, longitude, temperature, interest, email, telefone):  # Desafio 1., Desafio 2.
        if not self.validate_email(email):  # Desafio 2.
            raise ValueError("E-mail inválido!")  # Desafio 2.
        if not self.validate_telefone(telefone):  # Desafio 2.
            raise ValueError("Telefone inválido!")  # Desafio 2.
        if Lead.query.filter_by(email=email).first():  # Desafio 2.
            raise ValueError("E-mail já cadastrado!")  # Desafio 2.

        lead = Lead(name=name, latitude=latitude, longitude=longitude, temperature=temperature, interest=interest, email=email, telefone=telefone)  # Desafio 1., Desafio 2.
        self.db.session.add(lead)
        self.db.session.commit()

    def update_lead(self, lead_id, name, latitude, longitude, temperature, interest, email, telefone):  # Desafio 1., Desafio 2.
        lead = self.get_lead_by_id(lead_id)

        if not self.validate_email(email):  # Desafio 2.
            raise ValueError("E-mail inválido!")  # Desafio 2.
        if not self.validate_telefone(telefone):  # Desafio 2.
            raise ValueError("Telefone inválido!")  # Desafio 2.
        if Lead.query.filter_by(email=email).first() and lead.email != email:  # Desafio 2.
            raise ValueError("E-mail já cadastrado!")  # Desafio 2.

        lead.name = name
        lead.latitude = latitude
        lead.longitude = longitude
        lead.temperature = temperature
        lead.interest = interest
        lead.email = email  # Desafio 1., Desafio 2.
        lead.telefone = telefone  # Desafio 1., Desafio 2.
        self.db.session.commit()

    def get_all_leads(self):
        return Lead.query.all()

    def get_lead_by_id(self, lead_id):
        return Lead.query.get_or_404(lead_id)

    def delete_lead(self, lead_id):
        lead = self.get_lead_by_id(lead_id)
        self.db.session.delete(lead)
        self.db.session.commit()
