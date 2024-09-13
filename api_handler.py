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

    def get_leads(self):  # Rota de listagem de leads com paginação
        page = request.args.get('page', 1, type=int)  # Desafio 3.
        per_page = request.args.get('per_page', 10, type=int)  # Desafio 3.
        search_name = request.args.get('name', None, type=str)  # Desafio 4: Obtendo o nome da query string
        leads_pagination = self.lead_service.get_leads(page, per_page, search_name)  # Desafio 4: Passando o search_name para o serviço
        leads = [{
            'id': lead.id,
            'name': lead.name,
            'latitude': lead.latitude,
            'longitude': lead.longitude,
            'temperature': lead.temperature,
            'interest': lead.interest,
            'email': lead.email,  # Desafio 1.
            'telefone': lead.telefone  # Desafio 1.
        } for lead in leads_pagination.items]  # Desafio 3.

        return jsonify({
            'leads': leads,  # Desafio 3.
            'total': leads_pagination.total,  # Desafio 3.
            'pages': leads_pagination.pages,  # Desafio 3.
            'current_page': leads_pagination.page,  # Desafio 3.
            'per_page': leads_pagination.per_page  # Desafio 3.
        })

    def get_lead(self, id):
        lead = self.lead_service.get_lead_by_id(id)
        return jsonify(lead.as_dict())

    def create_lead(self):  # Operação de criação de lead
        data = request.json
        try:
            self.lead_service.create_lead(
                name=data['name'],
                latitude=data['latitude'],
                longitude=data['longitude'],
                temperature=data['temperature'],
                interest=data['interest'],
                email=data['email'],  # Desafio 1.
                telefone=data['telefone']  # Desafio 1.
            )
            return jsonify({"message": "Lead criado com sucesso!"}), 201
        except ValueError as e:  # Desafio 2.
            return jsonify({"error": str(e)}), 400  # Desafio 2.

    def update_lead(self, id):  # Operação de atualização de lead
        data = request.json
        try:
            self.lead_service.update_lead(
                lead_id=id,
                name=data['name'],
                latitude=data['latitude'],
                longitude=data['longitude'],
                temperature=data['temperature'],
                interest=data['interest'],
                email=data['email'],  # Desafio 1.
                telefone=data['telefone']  # Desafio 1.
            )
            return jsonify({"message": "Lead atualizado com sucesso!"})
        except ValueError as e:  # Desafio 2.
            return jsonify({"error": str(e)}), 400  # Desafio 2.

    def delete_lead(self, id):
        self.lead_service.delete_lead(id)
        return jsonify({"message": "Lead deletado com sucesso!"})
