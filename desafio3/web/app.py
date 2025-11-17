from flask import Flask
import os
import psycopg2
from redis import Redis, RedisError
import time

app = Flask(__name__)

# Função para tentar conectar ao banco de dados (Postgres)
def get_db_connection():
    # Os nomes 'db' e 'cache' são os NOMES DOS SERVIÇOS no docker-compose.yml
    db_host = os.environ.get('DB_HOST', 'db')
    db_pass = os.environ.get('DB_PASSWORD', 'minhasenha')
    db_user = os.environ.get('DB_USER', 'postgres') # Usuário padrão do postgres
    
    try:
        # Tenta conectar por 5 segundos
        conn = psycopg2.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            connect_timeout=5
        )
        return True, "Conexão com PostgreSQL bem-sucedida!"
    except Exception as e:
        return False, f"Erro ao conectar ao PostgreSQL: {str(e)}"

# Função para tentar conectar ao cache (Redis)
def get_redis_connection():
    cache_host = os.environ.get('CACHE_HOST', 'cache')
    
    try:
        # Tenta conectar e incrementar um contador
        redis_conn = Redis(host=cache_host, port=6379, socket_connect_timeout=5)
        count = redis_conn.incr('hits')
        return True, f"Conexão com Redis bem-sucedida! (Visitante nº {count})"
    except RedisError as e:
        return False, f"Erro ao conectar ao Redis: {str(e)}"

@app.route('/')
def hello():
    time.sleep(2) 
    
    db_ok, db_msg = get_db_connection()
    redis_ok, redis_msg = get_redis_connection()

    return f"""
    <h1>Status da Orquestração (Desafio 3)</h1>
    <p><strong>DB (PostgreSQL):</strong> {db_msg}</p>
    <p><strong>Cache (Redis):</strong> {redis_msg}</p>
    """

if __name__ == '__main__':
    # Roda na porta 5000
    app.run(host='0.0.0.0', port=5000)