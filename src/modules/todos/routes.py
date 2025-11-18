from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .services import TodoService

todos_bp = Blueprint('todos', __name__, url_prefix='/todos')

@todos_bp.route('/', methods=['POST'])
@jwt_required()
def create():
    """
    Criar uma nova tarefa
    ---
    tags:
      - Todos
    security:
      - Bearer: []
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - title
          properties:
            title:
              type: string
              example: Estudar Python
            description:
              type: string
              example: Ler a documentação do Flask
    responses:
      201:
        description: Tarefa criada
      400:
        description: Erro de validação
    """
    user_id = get_jwt_identity()
    data = request.get_json()
    todo = TodoService.create(user_id, data)
    return jsonify(todo.to_dict()), 201

@todos_bp.route('/', methods=['GET'])
@jwt_required()
def list_all():
    """
    Listar tarefas com paginação e filtros
    ---
    tags:
      - Todos
    security:
      - Bearer: []
    parameters:
      - name: page
        in: query
        type: integer
        default: 1
        description: Número da página
      - name: limit
        in: query
        type: integer
        default: 10
        description: Itens por página
      - name: status
        in: query
        type: string
        enum: [pending, completed]
        description: Filtrar por status
    responses:
      200:
        description: Lista de tarefas recuperada
    """
    user_id = get_jwt_identity()
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    status = request.args.get('status')
    
    pagination = TodoService.list_all(user_id, page, limit, status)
    
    return jsonify({
        "data": [t.to_dict() for t in pagination.items],
        "meta": {
            "page": page,
            "total_pages": pagination.pages,
            "total_items": pagination.total
        }
    }), 200

@todos_bp.route('/<int:todo_id>', methods=['PUT'])
@jwt_required()
def update_task(todo_id):
    """
    Atualizar uma tarefa existente
    ---
    tags:
      - Todos
    security:
      - Bearer: []
    parameters:
      - name: todo_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            title:
              type: string
            description:
              type: string
            is_completed:
              type: boolean
    responses:
      200:
        description: Tarefa atualizada
      404:
        description: Tarefa não encontrada
    """
    user_id = get_jwt_identity()
    data = request.get_json()
    updated_todo = TodoService.update(user_id, todo_id, data)
    return jsonify(updated_todo.to_dict()), 200

@todos_bp.route('/<int:todo_id>', methods=['DELETE'])
@jwt_required()
def delete(todo_id):
    """
    Deletar uma tarefa
    ---
    tags:
      - Todos
    security:
      - Bearer: []
    parameters:
      - name: todo_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Tarefa deletada com sucesso
      404:
        description: Tarefa não encontrada
    """
    user_id = get_jwt_identity()
    TodoService.delete(user_id, todo_id)
    return jsonify({"msg": "Tarefa deletada"}), 200