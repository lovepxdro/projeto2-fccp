# Desafio 1: Containers em rede

O objetivo deste desafio é criar dois containers Docker que se comunicam através de uma rede Docker customizada. Um container (Servidor) executa um servidor web na porta 8080, e o outro (Cliente) realiza requisições HTTP periódicas para o servidor.

## Arquitetura e decisões técnicas

```text
/desafio1
├── /cliente
│   ├── Dockerfile
│   └── start.sh
├── /servidor
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
└── README.md
```

A solução foi dividida em dois serviços independentes, cada um com seu próprio `Dockerfile`.

1. O servidor expõe um endpoint `/` na porta 8080. Cada vez que é acessado, retorna uma mensagem JSON e registra a requisição em seus logs. Seu container é baseado em `python:3.10-slim` para ser leve. Por ser o único serviço que requer uma instalação externa, o `requierements.txt` fica dentro dele.

2. O cliente é uma imagem `alpine` (extremamente leve) com `curl` instalado. Ele utiliza um script `start.sh` para rodar um loop infinito. A cada 3 segundos, ele faz uma requisição `curl` para o `servidor-app` na porta 8080. A escolha de usar um script em `.sh` ao invés de `.py` baseou-se na pouca complexidade da tarefa (rodar `curl` em loop). O `Dockerfile` apenas instala o `curl`, copia o script e o executa.
> OBS: Esta sugestão foi uma recomendação feita por IA.

3. Foi utilizada uma rede do tipo `bridge` customizada. Em vez de usar a rede `default` do Docker, criar uma rede nomeada é crucial. Isso ativa o **DNS interno do Docker**, permitindo que o container "Cliente" encontre o container "Servidor" simplesmente pelo seu nome (`servidor-app`), sem precisar saber o seu endereço IP.
> OBS: Esta sugestão foi uma recomendação feita por IA.

## Como executar

Antes de executar os comandos, certifique-se de estar dentro da pasta `desafio1`. Além disso, para quem for executar em ambiente `Windows`, pode acontecer do formato do arquivo `start.sh` **não** estar em **LF**, você pode verificar e alterar isso dentro do arquivo no canto inferior direito.

1. Criar rede docker. Para essa etapa foi usado o nome `minha-rede-desafio1`.
```bash
docker network create minha-rede-desafio1
```

2. Gerar o build das imagens.
```bash
docker build -t meu-servidor-app ./servidor
docker build -t meu-cliente-app ./cliente
```

3. Rodar o servidor em segundo plano.
```bash
docker run -d --name servidor-app --network minha-rede-desafio1 meu-servidor-app
```

4. Rodar o cliente (sem ser em segundo plano).
```bash
docker run --name cliente-app --network minha-rede-desafio1 meu-cliente-app
```

Para encerrar o cliente basta digitar `CTRL + C`.

## Logs

Caso tudo tenha funcionado corretamente (e o cliente não tenha sido executado em segundo plano), você deve estar vendo os logs do cliente. Algo como:

```
Cliente iniciando... aguardando 5s para o servidor...
Iniciando loop de requisições para http://servidor-app:8080
---------------------------------
(2025-11-15T18:00:05): Enviando requisição...
{"message":"Olá! Sou o Servidor (Container A) e estou na porta 8080."}
---------------------------------
(2025-11-15T18:00:08): Enviando requisição...
{"message":"Olá! Sou o Servidor (Container A) e estou na porta 8080."}
---------------------------------
```

**Conclusão:** Cliente se conectou com o servidor.

### Logs do servidor

Caso queira ver os logs do servidor, abra um novo terminal e execute:

```bash
docker logs -f servidor-app
```

## Limpando o ambiente

Ao final dos testes, execute os comandos para limpar o ambiente.

```bash
docker stop servidor-app cliente-app
docker rm servidor-app cliente-app
docker network rm minha-rede-desafio1
```