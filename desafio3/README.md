# Desafio 3

O objetivo deste desafio é usar o **Docker Compose** para orquestrar uma aplicação com múltiplos serviços dependentes. A aplicação é composta por três serviços:

1.  **`web`**: Um serviço de API em Python/Flask.
2.  **`db`**: Um banco de dados PostgreSQL.
3.  **`cache`**: Um cache em memória (Redis).

O Docker Compose é responsável por criar a rede interna, subir os serviços na ordem correta (`depends_on`) e injetar as variáveis de ambiente necessárias.

## Arquitetura e decisões

```text
/desafio3
├── /web                  (Código-fonte do serviço 'web')
│   ├── app.py            (App Flask que conecta no DB e Cache)
│   ├── Dockerfile        (Instruções para buildar o 'web')
│   └── requirements.txt  (Flask, psycopg2-binary, redis)
├── docker-compose.yml    (O "maestro" da orquestração)
└── README.md
```

## Como executar

Como esse desafio possui um `docker-compose` a execução é simplificada. Mas antes, certifique-se de estar dentro da pasta do desafio.

1. Subir a aplicação.

```bash
docker-compose up --build
```

2. Abrir `http://localhost:5000` para visualizar a aplicação.

## Limpando o ambiente

Volte ao terminal e que o `docker-compose` está rodando, digite `CTRL + C` e em seguida execute o comando:

```bash
docker-compose down
```