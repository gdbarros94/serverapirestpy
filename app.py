from flask import Flask
from database import DatabaseConnection
from api_handler import LeadAPIHandler
from flask_jwt_extended import JWTManager  #desafio 5. Importando JWTManager

# Configuração básica do Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  #desafio 5. Definindo a chave secreta para o JWT

# Inicializando a conexão com o banco de dados
db_connection = DatabaseConnection(app)
db_connection.initialize_db(app)

# Inicializando a autenticação JWT
jwt = JWTManager(app)  #desafio 5. Inicializando o JWTManager

# Inicializando a API com as rotas
api_handler = LeadAPIHandler(app, db_connection.get_db())

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
