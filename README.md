# API REST - mês dElas

API REST desenvolvida durante o evento mês dElas (edição 2022), produzido pelo grupo `Elas Computação`. 

> É usado Flask + python para criação e manipulação de TODO-list

## Funcionalidades

* Criação de lista

```
POST /list
```

* Listagem de listas

```
GET /lists
```

* Remoção de lista

```
DELETE /list/<id>
```

* Edição de lista

```
PUT /list/id
```

## Como executar a aplicação

Faça clone do repositório e instale as dependências com o comando

```bash
pip install -r requirements.txt
```

Após isso, basta iniciar o servidor com o comando

```
python -m servertodolist
```

A sua aplicação será iniciada em `http://localhost:8000` 