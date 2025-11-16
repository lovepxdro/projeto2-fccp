# Desafio 2

O objetivo deste desafio é demonstrar a persistência de dados em Docker. Para isso, criamos um container com um banco de dados PostgreSQL e utilizamos um **Volume Docker** para armazenar os dados fora do ciclo de vida do container.

O teste principal consiste em:
1.  Criar um container e um volume.
2.  Escrever dados no banco.
3.  Remover o container (mas não o volume).
4.  Criar um *novo* container, conectando-o ao volume existente.
5.  Provar que os dados originais ainda existem.

## Arquitetura e decisões técnicas

```text
/desafio2
├── screenshots
└── README.md
```

Para este desafio não é necessário desenvolver uma aplicação, apenas provar que os dados devem viver de forma independente do container, e isso pode ser feito usando a imagem do `postgres` direto do docker.
> OBS: Esta sugestão foi uma recomendação feita por IA.

1. Em vez de mapear uma pasta do host, usamos um **volume nomeado**. A imagem do PostgreSQL armazena todos os seus dados no diretório `/var/lib/postgresql/data` dentro do container. Mapeamos nosso volume nomeado para esse *path* exato.

## Como executar

Antes de executar os comandos, certifique-se de estar dentro da pasta `desafio2`.

1. Criar o volume docker.
> Primeiro, criamos o volume onde os dados do banco serão armazenados no host. Usaremos `meus-dados-bd` por praticidade.

```bash
docker volume create meus-dados-db
```

2. Subir o primeiro container.
> Subimos o primeiro container do postgreSQL. Definimos uma senha obrigatória e conectamos o volume que criamos ao diretório de dados do container.

```bash
docker run -d --name postgres-container-A -e POSTGRES_PASSWORD=minhasenha -v meus-dados-db:/var/lib/postgresql postgres
```

Pontos importantes desse comando:
- Após executar esse comando pode ser que seja necessário a instalação da biblioteca. Se o container não for criado ao final, limpe o ambiente e comece de novo (etapa 4 para limpar o container e etapa 7 para limpar o volume).
- Antes de executar o próximo comando, verifique se o container está rodando com `docker ps`.

3. Criar o banco de dados.
> Agora nos conectamos ao container e criamos uma tabela de testes.

```bash
docker exec -it postgres-container-A psql -U postgres
```
Ao executar esse comando entramos ao shell interativo do psql. A partir dele podemos executar querys. A ordem dos comandos realizará as seguintes ações:
- Criar uma tabela.
- Inserir um dado.
- Verificar se o dado foi inserido. Opcional, mas recomendado.

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100)
);
```

```sql
INSERT INTO usuarios (nome) VALUES ('Pedro');
```

```sql
SELECT * FROM usuarios;
```
![provaA](desafio2\screenshots\A.png)

Para sair do shell psql digite `\q`.

4. Destruir o primeiro container.
> Agora que inserirmos um dado nesse container, vamos destruir ele. Os dados, que estão no volume, devem ficar intactos.

```bash
docker stop postgres-container-A
docker rm postgres-container-A
```

Nesse momento, o container A não existe mais.

5. Subir um novo container.
> Vamos criar um novo container e conectá-lo ao mesmo volume, que não foi destruido.

```bash
docker run -d --name postgres-container-B -e POSTGRES_PASSWORD=minhasenha -v meus-dados-db:/var/lib/postgresql postgres
```

```bash
docker exec -it postgres-container-B psql -U postgres
```

6. Verificar os dados
> Após criar o novo container e conectar ele ao volume, vamos exibir os dados do volume. Dentro do shell psql, execute:

```sql
SELECT * FROM usuarios;
```
![provaB](desafio2\screenshots\B.png)

Lembre que o comando para sair desse shell é `\q`.

7. Limpeza do ambiente
> Após os testes, vamos remover tanto o container B quanto o volume.

```bash
docker stop postgres-container-B
docker rm postgres-container-B

docker volume rm meus-dados-db
```

**Conclusão:** O volume existe de maneira independente do container.
