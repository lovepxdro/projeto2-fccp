from flask import Flask, jsonify

app = Flask(__name__)

# Dados mocados (simulados) para o Microsserviço A
_USERS = [
    {"id": 1, "nome": "Ana", "ativo_desde": "2023-01-15"},
    {"id": 2, "nome": "Bruno", "ativo_desde": "2024-03-10"},
    {"id": 3, "nome": "Carla", "ativo_desde": "2022-11-30"}
]

@app.route('/users')
def get_users():
    """Endpoint que retorna a lista de usuários."""
    app.logger.info("Serviço A: Requisição /users recebida.")
    return jsonify(_USERS)

if __name__ == '__main__':
    # Roda na porta 5001 (porta interna)
    app.run(host='0.0.0.0', port=5001)