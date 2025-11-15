#!/bin/sh

echo "Cliente iniciando... aguardando 5s para o servidor..."
sleep 5

# O nome 'servidor-app' é o nome do container do servidor, definido no comando 'docker run'.
# O Docker usará sua rede customizada para resolver esse nome para o IP correto.
SERVER_URL="http://servidor-app:8080"

echo "Iniciando loop de requisições para $SERVER_URL"

while true
do
    echo "---------------------------------"
    echo "$(date): Enviando requisição..."

    curl -s $SERVER_URL
    
    echo "\n---------------------------------"
    
    sleep 3
done