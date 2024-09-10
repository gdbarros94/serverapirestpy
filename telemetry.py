import json
from flask import request, jsonify
from datetime import datetime
import os

class Telemetry:
    def __init__(self, log_file='telemetry.txt'):
        self.log_file = log_file
        # Cria o arquivo de log se não existir
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as file:
                json.dump([], file)

    def log_request(self, status_code):
        # Captura dados da requisição
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "ip": request.remote_addr,
            "method": request.method,
            "endpoint": request.path,
            "status_code": status_code,
            "user_agent": request.user_agent.string,
            # Removido `request.elapsed` porque não existe no Flask
            "latency": None  
        }

        # Lê o arquivo de log e adiciona o novo registro
        with open(self.log_file, 'r+') as file:
            logs = json.load(file)
            logs.append(log_data)
            file.seek(0)
            json.dump(logs, file, indent=4)

    def read_logs(self):
        # Retorna os logs em formato JSON
        with open(self.log_file, 'r') as file:
            return json.load(file)

# Uso no app Flask
from flask import Flask, jsonify

app = Flask(__name__)
telemetry = Telemetry()

@app.after_request
def log_telemetry(response):
    # Após cada requisição, registrar os dados de telemetria
    telemetry.log_request(response.status_code)
    return response

# Rota para exibir os logs
@app.route('/telemetry', methods=['GET'])
def get_telemetry_logs():
    logs = telemetry.read_logs()
    return jsonify(logs)