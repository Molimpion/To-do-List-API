# 🐍 Todo List API (Desafio Roadmap.sh)

-----

*Este projeto é a implementação do desafio **Todo List API** do [roadmap.sh](https://roadmap.sh/projects/todo-list-api), construído com foco em **Arquitetura Modular (Service Pattern)** e **Qualidade de Código**.*

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,flask,mysql,docker,swagger,pytest" />
  </a>
</div>


## 1\. Visão Geral e Estado do Projeto

Este repositório contém uma **API RESTful** completa para gerenciamento de tarefas pessoais. O objetivo principal foi cumprir o desafio do roadmap.sh e, adicionalmente, aplicar padrões de projetos vistos no mercado (como Service Pattern e Logs estruturados).

Todos os requisitos funcionais do backend foram **concluídos, documentados com Swagger e validados por testes automatizados**.

  * [x] **Funcionalidade Central (CRUD):** Completo
  * [x] **Autenticação (JWT):** Completo
  * [x] **Paginação e Filtros:** Completo
  * [x] **Testes Automatizados (Pytest):** Completo
  * [x] **Documentação Interativa (Swagger):** Completo
  * [x] **Arquitetura Modular (Service Pattern):** Completo

-----

## 2\. Arquitetura e Decisões de Design

A aplicação segue o padrão **Modular (Feature-Based)** para maximizar a testabilidade e o reuso de código:

  * **Padrão Service:** Toda a lógica de negócio (*hashing*, validação de dados, consultas ao banco) está isolada na camada **Service**. As rotas (`routes.py`) apenas lidam com a camada HTTP.
  * **Tratamento de Erros:** Sistema centralizado no `__init__.py` que captura todas as exceções personalizadas (`AuthError`, `NotFoundError`) e as transforma em respostas JSON padronizadas.
  * **Banco de Dados:** MySQL 8.0, orquestrado via **Docker Compose**.
  * **Developer Experience (DX):** Uso da biblioteca **Rich** para logs coloridos e tracebacks formatados no terminal.
  * **QA:** Uso de **Pytest** com banco de dados SQLite em memória (`:memory:`) para garantir que os testes sejam rápidos e isolados.

-----

## 3\. Como Executar o Projeto Localmente

O ambiente é padronizado via Docker para o banco de dados e o Python roda em `venv`.

### 1\. Pré-requisitos

  * Git
  * Docker e Docker Compose (para o MySQL)
  * Python 3.10+ e `venv`

### 2\. Setup e Inicialização

1.  **Clone o repositório, crie e ative o ambiente virtual.**
2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Crie o arquivo `.env`** na raiz do projeto (importante para as credenciais).
4.  **Inicie o Banco de Dados (MySQL):**
    ```bash
    docker-compose up -d
    ```
5.  **Inicie a Aplicação Flask:**
    ```bash
    python run.py
    ```
    *O terminal mostrará um link clicável para a documentação via Rich.*

-----

## 4\. Testes e Documentação

### 4.1. Testes Automatizados (Pytest) 🧪

Para executar o conjunto de testes (8 testes unitários e de integração), use o comando com `PYTHONPATH` para resolver as importações modulares:

```bash
PYTHONPATH=. pytest
```

*A saída deve ser `8 passed`, confirmando a estabilidade do sistema.*

### 4.2. Documentação Interativa (Swagger UI) 📄

A documentação visual e interativa está disponível em: `http://127.0.0.1:5000/docs`

1.  **Login:** Use o endpoint `/auth/login` para obter o `access_token`.
2.  **Autorização:** Clique em **"Authorize"** e insira o token no formato: `Bearer [SEU_TOKEN_AQUI]`.
3.  Execute o CRUD completo na interface do Swagger.

-----

## 5\. Endpoints Principais

| Método | Endpoint | Descrição | Segurança |
| :--- | :--- | :--- | :--- |
| `POST` | `/auth/register` | Cria um novo usuário | Público |
| `POST` | `/auth/login` | Autentica e retorna o JWT | Público |
| `POST` | `/todos` | Cria uma nova tarefa | **Token Obrigatório** |
| `GET` | `/todos` | Lista tarefas (com Paginação e Filtros `?status=`) | **Token Obrigatório** |
| `PUT` | `/todos/{id}` | Atualiza o conteúdo ou status (`is_completed`) | **Token Obrigatório** |
| `DELETE` | `/todos/{id}` | Remove uma tarefa | **Token Obrigatório** |

