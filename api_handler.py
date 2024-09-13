from flask import Flask, jsonify, request
from flask_jwt_extended import jwt_required  #desafio 5. Importando jwt_required para proteger as rotas
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
	
    @jwt_required() #demostracao
    def get_leads(self):  
        page = request.args.get('page', 1, type=int)  
        per_page = request.args.get('per_page', 10, type=int)  
        leads_pagination = self.lead_service.get_leads(page, per_page)
        leads = [{
            'id': lead.id,
            'name': lead.name,
            'latitude': lead.latitude,
            'longitude': lead.longitude,
            'temperature': lead.temperature,
            'interest': lead.interest,
            'email': lead.email,
            'telefone': lead.telefone
        } for lead in leads_pagination.items]

        return jsonify({
            'leads': leads,
            'total': leads_pagination.total,
            'pages': leads_pagination.pages,
            'current_page': leads_pagination.page,
            'per_page': leads_pagination.per_page
        })

    def get_lead(self, id):
        lead = self.lead_service.get_lead_by_id(id)
        return jsonify(lead.as_dict())

    @jwt_required()  #desafio 5. Protegendo a rota de criação de leads
    def create_lead(self):
        data = request.json
        try:
            self.lead_service.create_lead(
                name=data['name'],
                latitude=data['latitude'],
                longitude=data['longitude'],
                temperature=data['temperature'],
                interest=data['interest'],
                email=data['email'],
                telefone=data['telefone']
            )
            return jsonify({"message": "Lead criado com sucesso!"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @jwt_required()  #desafio 5. Protegendo a rota de atualização de leads
    def update_lead(self, id):
        data = request.json
        try:
            self.lead_service.update_lead(
                lead_id=id,
                name=data['name'],
                latitude=data['latitude'],
                longitude=data['longitude'],
                temperature=data['temperature'],
                interest=data['interest'],
                email=data['email'],
                telefone=data['telefone']
            )
            return jsonify({"message": "Lead atualizado com sucesso!"})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @jwt_required()  #desafio 5. Protegendo a rota de deleção de leads
    def delete_lead(self, id):
        self.lead_service.delete_lead(id)
        return jsonify({"message": "Lead deletado com sucesso!"})
