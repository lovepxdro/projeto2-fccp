# Desafio 4

O objetivo deste desafio é implementar uma comunicação síncrona via HTTP entre dois microsserviços distintos, onde um consome dados do outro.

## Arquitetura e decisões técnicas

```text
/desafio4
├── /servico-a-usuarios
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── /servico-b-usuarios
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

A lógica baseia-se na separação de responsabilidades. Temos um serviço que detém os dados (A) e outro que detém a lógica de apresentação (B). A comunicação ocorre via requisições HTTP diretas dentro da rede interna do Docker.

Serviço A (API): Uma API Flask simples que retorna um JSON na rota /users. Ele não se preocupa com quem consome os dados, apenas os disponibiliza.

Serviço B (Front/Processador): Este serviço atua como cliente do Serviço A. Ao receber um acesso do usuário, ele utiliza a biblioteca requests do Python para disparar uma chamada GET http://servico-a:5001/users. Ele processa o JSON recebido e renderiza o HTML final para o usuário.

## Como executar

1. Subir os serviços:
```bash
docker-compose up --build
```

2. Testar: Acesse **http://localhost:5002**. O Serviço B irá buscar os dados no Serviço A e exibi-los formatados.

3. Encerrar (Lembre de digitar ``CTRL + C`` para sair do terminal docker):
```bash
docker-compose down
```