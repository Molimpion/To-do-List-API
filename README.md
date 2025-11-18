Com certeza\! Vamos estruturar o **README.md** do seu projeto de **Todo List API** para que ele tenha a mesma qualidade profissional e detalhamento técnico do projeto S.O.R.O., destacando suas escolhas de arquitetura (Modular, Service Pattern) e qualidade (Testes, Swagger).

-----

# 📝 Repositório da Todo List API (Roadmap.sh Challenge)

-----

*Este projeto é a implementação do desafio **Todo List API** do [roadmap.sh](https://roadmap.sh/projects/todo-list-api), construído com foco em **Arquitetura Modular (Service Pattern)** e **Qualidade de Código**.*

        [](https://www.google.com/search?q=/docs)

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

A aplicação segue uma arquitetura modular, dividida por funcionalidades (*features*), o que garante alta **cobertura de testes** e facilidade de manutenção.

  * **Padrão de Arquitetura:** **Modular (Feature-Based)**. A separação em módulos (`auth`, `todos`) e o uso do **Service Pattern** garantem que a lógica de negócio (*hashing* de senha, regras de filtragem) esteja totalmente desacoplada das rotas HTTP.
  * **Decisão de Stack:** Python com Flask foi escolhido por sua leveza e flexibilidade, ideal para microserviços.
  * **Banco de Dados:** MySQL 8.0, orquestrado via **Docker Compose** para isolamento e ambiente padronizado.
  * **Segurança:** Implementação de tokens **JWT** para autenticação e `werkzeug.security` para criptografia de senhas.
  * **Tratamento de Erros:** Sistema centralizado no `__init__.py` que captura todas as exceções personalizadas (`APIError`, `AuthError`, `NotFoundError`) e as transforma em respostas JSON padronizadas.
  * **Developer Experience (DX):** Uso da biblioteca **Rich** para logs coloridos e tracebacks legíveis no terminal, e **Flasgger** para documentação interativa.

-----

## 3\. Como Executar o Projeto Localmente

O ambiente de desenvolvimento é padronizado via Docker para garantir que funcione em qualquer máquina ou no GitHub Codespaces.

### 1\. Pré-requisitos

  * Git
  * Docker e Docker Compose
  * Python 3.10+
  * Ambiente Virtual (`venv`)

### 2\. Inicialização

1.  Clone o repositório.

2.  Crie e ative o ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4.  Crie o arquivo de variáveis de ambiente **`.env`** na raiz do projeto (use o exemplo a seguir como guia, alterando apenas os valores de segredo):

    ```env
    # --- Configurações do Flask e JWT ---
    FLASK_APP=src.__init__.py
    FLASK_DEBUG=1
    SECRET_KEY=sua_chave_secreta
    JWT_SECRET_KEY=sua_chave_jwt_secreta

    # --- Configurações do Banco de Dados (MySQL) ---
    MYSQL_ROOT_PASSWORD=root_super_secure_password
    MYSQL_DATABASE=todo_db
    MYSQL_USER=app_user
    MYSQL_PASSWORD=app_password
    MYSQL_HOST=127.0.0.1
    MYSQL_PORT=3306
    DATABASE_URL=mysql+mysqlconnector://${MYSQL_USER}:${MYSQL_PASSWORD}@${MYSQL_HOST}:${MYSQL_PORT}/${MYSQL_DATABASE}
    ```

5.  **Inicie o Banco de Dados (MySQL):**

    ```bash
    docker-compose up -d
    ```

6.  **Inicie a Aplicação Flask:**

    ```bash
    python run.py
    ```

    *A aplicação criará as tabelas automaticamente e o terminal exibirá um link clicável para a documentação.*

-----

## 4\. Testes e Documentação

### 4.1. Documentação Interativa (Swagger UI) 📄

Acesse a documentação no seu navegador, adicionando `/docs` à porta da sua aplicação (ex: `http://127.0.0.1:5000/docs`).

1.  Clique no botão **"Authorize"**.
2.  No campo **Value**, insira o token recebido no Login com o prefixo ` Bearer  `:
    `Bearer [SEU_TOKEN_AQUI]`
3.  Execute os endpoints diretamente na interface.

### 4.2. Testes Automatizados (Pytest) 🧪

O projeto possui 8 testes de integração e unidade configurados para rodarem com um banco SQLite temporário.

1.  Execute os testes a partir da raiz do projeto:
    ```bash
    PYTHONPATH=. pytest
    ```
2.  A saída deve indicar **8 passed**, garantindo que as regras de negócio e a segurança do JWT estão operando corretamente.

### 4.3. Testes Manuais (REST Client)

O arquivo `testes/api.http` contém todo o fluxo de ponta a ponta (Registro, Login, CRUD, Filtros) para testes rápidos via extensão **REST Client** (VS Code).

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
