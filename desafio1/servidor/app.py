from flask import Flask, jsonify
import logging

# Configura o logging para vermos as saídas no 'docker logs'
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def home():
    # Log para o console do container
    app.logger.info("Requisição recebida na rota '/'")
    return jsonify(message="Olá! Sou o Servidor (Container A) e estou na porta 8080."), 200

if __name__ == '__main__':
    # Roda o app na porta 8080, acessível por qualquer IP (0.0.0.0)
    app.run(host='0.0.0.0', port=8080)