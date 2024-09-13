from flask import jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

# Usuário e senha fictícios apenas para demonstração
USUARIO = 'admin'
SENHA = '123456'

class AuthHandler:
    def __init__(self, app):
        self.app = app
        self.app.add_url_rule('/login', view_func=self.login, methods=['POST'])

    def login(self):
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Autenticação simples com um usuário fixo
        if username == USUARIO and check_password_hash(SENHA, password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"error": "Credenciais inválidas!"}), 401
