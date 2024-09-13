from models import Lead

class LeadService:
	def __init__(self, db):
		self.db = db

	def create_lead(self, name, latitude, longitude, temperature, interest, email, telefone): #desafio 1.
		lead = Lead( #desafio 1.
			name=name, #desafio 1.
			latitude=latitude, #desafio 1.
			longitude=longitude, #desafio 1.
			temperature=temperature, #desafio 1.
			interest=interest, #desafio 1.
			email=email, #desafio 1.
			telefone=telefone #desafio 1.
		) 
		self.db.session.add(lead)
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
