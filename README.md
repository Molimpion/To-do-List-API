# 🐍 Todo List API (Desafio Roadmap.sh)

*Implementação do desafio **Todo List API** do [roadmap.sh](https://roadmap.sh/projects/todo-list-api), usando **Arquitetura Modular (Service Pattern)** e foco em **qualidade de código**.*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black) ![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

## 1. Visão Geral e Estado do Projeto

API RESTful para gerenciamento de tarefas pessoais, cumprindo todos os requisitos do desafio. Todas as funcionalidades foram concluídas, documentadas via Swagger e validadas com testes automatizados.

* [x] CRUD
* [x] Autenticação (JWT)
* [x] Paginação e filtros
* [x] Testes automatizados
* [x] Documentação Swagger
* [x] Arquitetura Modular (Service Pattern)

## 2. Arquitetura e Decisões

* Separação por módulos (features)
* Service Pattern
* Flask + Python
* MySQL 8 (Docker Compose)
* Autenticação JWT
* Handler de erros centralizado
* DX com Rich e Flasgger

---

## 3. Como Executar Localmente

Ambiente padronizado via Docker (MySQL) e Python em `venv`.

### Pré-requisitos

Git · Docker/Compose · Python 3.10+ com venv

### Setup

1. Clone o repositório e entre na pasta:
   ```bash
   git clone [https://github.com/seu-usuario/todo-list-api.git](https://github.com/seu-usuario/todo-list-api.git)
   cd todo-list-api
````

2.  Crie e ative o ambiente virtual:

    ```bash
    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Windows (PowerShell)
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4.  Crie o arquivo `.env` na raiz (use o `.env.example` como base se houver)

5.  Inicie o banco de dados:

    ```bash
    docker-compose up -d
    ```

6.  Inicie a aplicação:

    ```bash
    python run.py
    ```

-----

## 4\. Testes e Documentação

### Testes (Pytest)

```bash
PYTHONPATH=. pytest
```

*Saída esperada: `8 passed`.*

### Documentação (Swagger UI)

Disponível em `http://127.0.0.1:5000/docs`.

1.  Use `/auth/login` para obter o `access_token`.
2.  Clique em **Authorize** → `Bearer [TOKEN]`.
3.  Execute o CRUD pela interface.

-----

## 5\. Endpoints Principais

| Método | Endpoint         | Descrição                         | Segurança         |
| ------ | ---------------- | --------------------------------- | ----------------- |
| POST   | `/auth/register` | Cria usuário                      | Público           |
| POST   | `/auth/login`    | Autentica e retorna JWT           | Público           |
| POST   | `/todos`         | Cria tarefa                       | Token obrigatório |
| GET    | `/todos`         | Lista tarefas (paginação/filtros) | Token obrigatório |
| PUT    | `/todos/{id}`    | Atualiza tarefa                   | Token obrigatório |
| DELETE | `/todos/{id}`    | Remove tarefa                     | Token obrigatório |
