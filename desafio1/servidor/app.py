from flask import Flask, jsonify
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def home():
    app.logger.info("Requisição recebida na rota '/'")
    return jsonify(message="Olá! Sou o Servidor (Container A) e estou na porta 8080."), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)