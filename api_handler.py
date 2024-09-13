from flask import Flask, jsonify, request
from lead_service import LeadService

class LeadAPIHandler:
	def __init__(self, app, db):
		self.app = app
		self.lead_service = LeadService(db)
		self.app.add_url_rule('/leads', view_func=self.get_leads, methods=['GET'])
		self.app.add_url_rule('/leads/<int:id>', view_func=self.get_lead, methods=['GET'])
		self.app.add_url_rule('/leads', view_func=self.create_lead, methods=['POST'])
		self.app.add_url_rule('/leads/<int:id>', view_func=self.update_lead, methods=['PUT'])
		self.app.add_url_rule('/leads/<int:id>', view_func=self.delete_lead, methods=['DELETE'])

	def get_leads(self):
		leads = self.lead_service.get_all_leads()
		return jsonify([lead.as_dict() for lead in leads])

	def get_lead(self, id):
		lead = self.lead_service.get_lead_by_id(id)
		return jsonify(lead.as_dict())

	def create_lead(self):
		data = request.json
		self.lead_service.create_lead( #desafio 1.
        	name=data['name'], #desafio 1.
        	latitude=data['latitude'], #desafio 1.
        	longitude=data['longitude'], #desafio 1.
        	temperature=data['temperature'], #desafio 1.
        	interest=data['interest'], #desafio 1.
        	email=data['email'], #desafio 1.
        	telefone=data['telefone'] #desafio 1.
    	)
		return jsonify({"message": "Lead criado com sucesso!"}), 201

	def update_lead(self, id):
		data = request.json
		self.lead_service.update_lead( #desafio 1.
        	lead_id=id, #desafio 1.
        	name=data['name'], #desafio 1.
        	latitude=data['latitude'], #desafio 1.
        	longitude=data['longitude'], #desafio 1.
        	temperature=data['temperature'], #desafio 1.
        	interest=data['interest'], #desafio 1.
        	email=data['email'], #desafio 1.
        	telefone=data['telefone'] #desafio 1.
    	)
		return jsonify({"message": "Lead atualizado com sucesso!"})

	def delete_lead(self, id):
		self.lead_service.delete_lead(id)
		return jsonify({"message": "Lead deletado com sucesso!"})
