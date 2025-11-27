# Desafio 5: Microsserviços com API gateway

O objetivo deste desafio é implementar o padrão de projeto **API Gateway**. Em vez de o cliente saber o endereço de cada microsserviço (Users e Orders), ele se comunica apenas com um ponto central (Gateway), que roteia as chamadas adequadamente.

## Arquitetura e decisões técnicas

```text
/desafio5
├── /gateway
│   ├── Dockerfile
│   └── nginx.conf
├── /orders
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── /users
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

Utilizamos o **Nginx** como API Gateway devido à sua performance e robustez como proxy reverso.
> OBS: Esta sugestão foi uma recomendação feita por IA.

Os serviços de backend consistem em duas APIs Flask independentes: uma para dados de usuários e outra para dados de pedidos. Ambos operam isolados na rede interna, sem exposição direta de portas ao host, reforçando a segurança do ambiente.

O API Gateway utiliza Nginx para escutar na porta interna 80, roteando /users para o container do serviço de usuários e /orders para o serviço de pedidos. Ele é o único componente exposto externamente, abrindo a porta 4000 para acesso ao sistema

## Como executar

1.  Subir a stack:
    ```bash
    docker-compose up --build
    ```

2.  Testar os endpoints:
    * **Usuários**: [http://localhost:4000/users](http://localhost:4000/users)
    * **Pedidos**: [http://localhost:4000/orders](http://localhost:4000/orders)
    * **Gateway Status**: [http://localhost:4000/](http://localhost:4000/)

3.  Encerrar (Lembre de digitar ``CTRL + C`` para sair do terminal docker):
    `docker-compose down`