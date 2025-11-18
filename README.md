# 📝 Todo List API (Roadmap.sh Challenge)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)
![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

Este projeto é a implementação do desafio Todo List API do [roadmap.sh](https://roadmap.sh/projects/todo-list-api), construído com foco em Arquitetura Modular (Service Pattern) e Qualidade de Código.

---

### 1. Visão Geral e Estado do Projeto

<!-- Lista de requisitos -->
- [x] Funcionalidade Central (CRUD)
- [x] Autenticação (JWT)
- [x] Paginação e Filtros
- [x] Testes Automatizados (Pytest)
- [x] Documentação Interativa (Swagger)
- [x] Arquitetura Modular (Service Pattern)

### 2. Arquitetura e Decisões de Design

- Separação por módulos (features)
- Service Pattern para lógica desacoplada
- Flask e Python para microserviços
- MySQL 8 via Docker Compose
- JWT para autenticação
- Handler de erros centralizados (__init__.py)
- DX: Rich, Flasgger

### 3. Como Executar

**Pré-requisitos:**
- Git, Docker (+Compose), Python 3.10+, venv

**Setup:**
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Configuração do .env:** (veja exemplo acima)

**Banco:**
```
docker-compose up -d
```

**Rodar API:**
```
python run.py
```

### 4. Testes e Documentação

- Acesse: http://127.0.0.1:5000/docs (Swagger)
- Testes automatizados: `PYTHONPATH=. pytest`
- Testes manuais: arquivo `api.http` para REST Client

### 5. Endpoints Principais

| Método | Endpoint        | Descrição                       | Segurança           |
|--------|----------------|---------------------------------|---------------------|
| POST   | /auth/register | Cria um novo usuário            | Público             |
| POST   | /auth/login    | Autentica e retorna o JWT       | Público             |
| POST   | /todos         | Cria uma nova tarefa            | Token Obrigatório   |
| GET    | /todos         | Lista tarefas                   | Token Obrigatório   |
| PUT    | /todos/{id}    | Atualiza tarefa/status          | Token Obrigatório   |
| DELETE | /todos/{id}    | Remove uma tarefa               | Token Obrigatório   |
```

***

## Versão 2: Visual Moderno com Skill Icons – Foco em Stack Imediato e Experiência

```markdown
# 📝 Todo List API (Roadmap.sh Challenge)

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,flask,mysql,docker,swagger,pytest" />
  </a>
</div>

Este projeto é a implementação do desafio Todo List API do [roadmap.sh](https://roadmap.sh/projects/todo-list-api), desenvolvido com arquitetura modular e código limpo.

---

### Visão Geral do Projeto

- API RESTful para tarefas pessoais
- Padrão Modular e Service Pattern implementados
- CRUD, autenticação JWT, filtros e testes
- Documentação Swagger + testes Pytest

---

### Arquitetura & Design

- **Módulos organizados:** auth e todos, isolamento em services
- **Banco:** MySQL 8.0, dockerizado
- **Autenticação:** JWT, segurança por werkzeug
- **DX:** Rich (logs), Flasgger (docs)

---

### Como Executar

**1. Pré-requisitos:**  
Git, Docker, Python >=3.10, venv

**2. Setup:**  
- Clone, crie venv e instale dependências
- Configure o arquivo `.env`  
- Suba o banco com `docker-compose up -d`  
- Rode `python run.py`

---

### Testes & Documentação

- Swagger: [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)  
- Testes: `PYTHONPATH=. pytest`  
- Testes manuais: arquivo `api.http` completo

---

### Endpoints Principais

| Método | Endpoint        | Descrição                       | Segurança           |
|--------|----------------|---------------------------------|---------------------|
| POST   | /auth/register | Cria um novo usuário            | Público             |
| POST   | /auth/login    | Autentica e retorna o JWT       | Público             |
| POST   | /todos         | Cria uma nova tarefa            | Token Obrigatório   |
| GET    | /todos         | Lista tarefas                   | Token Obrigatório   |
| PUT    | /todos/{id}    | Atualiza tarefa/status          | Token Obrigatório   |
| DELETE | /todos/{id}    | Remove uma tarefa               | Token Obrigatório   |
```

***

Essas duas estruturas estão entre as mais apreciadas em projetos open source de qualidade e vão valorizar ainda mais o seu repositório. Você pode alternar entre o visual mais “corporativo” do Shields.io ou o impacto moderno e direto dos Skill Icons, sempre com tabelas e divisão lógica das seções.[1][2][3][4][5]

[1](https://github.com/tandpfun/skill-icons)
[2](https://github.com/gui-bus/TechIcons)
[3](https://skillicons.dev)
[4](https://github.com/cfprocha/distintivos)
[5](https://apidog.com/pt/blog/api-documentation-best-practices-and-tools-pt/)
