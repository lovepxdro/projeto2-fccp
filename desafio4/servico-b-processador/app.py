from flask import Flask
import requests
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Pega a URL do Serviço A a partir das variáveis de ambiente
# O nome 'servico-a' é o nome DNS que o Docker Compose dá
USER_API_URL = os.environ.get('USER_API_URL', 'http://servico-a:5001/users')

@app.route('/')
def get_processed_user_report():
    """
    Consome o Serviço A (/users), processa os dados e exibe
    um relatório formatado.
    """
    app.logger.info(f"Serviço B: Recebida requisição. Tentando chamar {USER_API_URL}...")
    
    try:
        # 1. Fazer a requisição HTTP para o Microsserviço A
        response = requests.get(USER_API_URL)
        response.raise_for_status() # Lança um erro se a requisição falhar
        
        users = response.json()
        app.logger.info(f"Serviço B: Dados recebidos do Serviço A: {users}")
        
        # 2. Processar os dados e montar a resposta (conforme requisito)
        output = "<h1>Relatório de Usuários (processado pelo Serviço B)</h1>"
        output += "<p>Dados consumidos com sucesso do Serviço A.</p>"
        
        for user in users:
            # Ex: "Usuário X ativo desde..."
            output += f"<li>Usuário <b>{user['nome']}</b> (ID: {user['id']}) está ativo desde {user['ativo_desde']}.</li>"
            
        return f"<ul>{output}</ul>"

    except requests.exceptions.ConnectionError:
        msg = f"Erro: Não foi possível conectar ao Microsserviço A em {USER_API_URL}. O serviço está de pé?"
        app.logger.error(msg)
        return msg, 503 # Service Unavailable
        
    except Exception as e:
        msg = f"Erro interno no Serviço B: {str(e)}"
        app.logger.error(msg)
        return msg, 500

if __name__ == '__main__':
    # Roda na porta 5002 (porta interna e externa)
    app.run(host='0.0.0.0', port=5002)