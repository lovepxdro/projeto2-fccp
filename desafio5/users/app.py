from flask import Flask, jsonify

app = Flask(__name__)

users_db = [
    {"id": 1, "name": "Pedro", "email": "pedro@exemplo.com"},
    {"id": 2, "name": "Maria", "email": "maria@exemplo.com"}
]

@app.route('/users')
def get_users():
    return jsonify(users_db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)