# FastAPI CRUD Project

## Descrição

Este projeto é uma aplicação CRUD simples construída com FastAPI e SQLAlchemy, utilizando um banco de dados PostgreSQL. A aplicação permite criar, ler, atualizar e excluir cursos através de endpoints RESTful.

## Estrutura do Projeto

```plaintext
.
├── api
│   └── v1
│       └── endpoints
│           └── course.py
├── core
│   ├── configs.py
│   ├── database.py
│   └── deps.py
├── models
│   └── course_model.py
├── schemas
│   └── course_schema.py
├── main.py
├── tables.py
└── check_tables.py


Configuração
Pré-requisitos
Python 3.10+
PostgreSQL
Git
Instalando Dependências
Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


python -m venv .venv
source .venv/bin/activate  # No Windows use `.venv\Scripts\activate`


pip install -r requirements.txt


Configuração do Banco de Dados
Configure o banco de dados PostgreSQL e atualize a string de conexão no arquivo core/configs.py:
DB_URL: str = "postgresql+asyncpg://usuario:senha@localhost:5432/nome_do_banco"


Criando Tabelas
Execute o script para criar as tabelas:
python tables.py


Executando a Aplicação
Inicie o servidor FastAPI:

python -m uvicorn main:app --reload

Acesse a documentação da API:

Navegue até http://127.0.0.1:8000/docs para visualizar a documentação interativa da API.
Endpoints da API
POST /api/v1/courses/ - Cria um novo curso
GET /api/v1/courses/ - Retorna todos os cursos
GET /api/v1/courses/{course_id} - Retorna um curso específico pelo ID
PUT /api/v1/courses/{course_id} - Atualiza um curso específico pelo ID
DELETE /api/v1/courses/{course_id} - Exclui um curso específico pelo ID
Scripts Úteis
tables.py - Script para criar e limpar as tabelas do banco de dados
check_tables.py - Script para verificar a existência das tabelas no banco de dados
Contribuindo
Faça um fork do repositório.
Crie uma branch para sua feature (git checkout -b feature/fooBar).
Commit suas alterações (git commit -am 'Add some fooBar').
Push para a branch (git push origin feature/fooBar).
Crie um novo Pull Request.
Licença
Distribuído sob a licença MIT. Veja LICENSE para mais informações.

Contato
Seu Nome - @EdmilsonAlison - eddiasdev@gmail.com


