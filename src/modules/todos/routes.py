from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .services import TodoService

todos_bp = Blueprint('todos', __name__, url_prefix='/todos')

@todos_bp.route('/', methods=['POST'])
@jwt_required()
def create():
    user_id = get_jwt_identity()
    data = request.get_json()
    todo = TodoService.create(user_id, data)
    return jsonify(todo.to_dict()), 201

@todos_bp.route('/', methods=['GET'])
@jwt_required()
def list_all():
    user_id = get_jwt_identity()
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)

    pagination = TodoService.list_all(user_id, page, limit)

    return jsonify({
        "data": [t.to_dict() for t in pagination.items],
        "meta": {
            "page": page,
            "total_pages": pagination.pages,
            "total_items": pagination.total
        }
    }), 200

@todos_bp.route('/<int:todo_id>', methods=['DELETE'])
@jwt_required()
def delete(todo_id):
    user_id = get_jwt_identity()
    TodoService.delete(user_id, todo_id)
    return jsonify({"msg": "Tarefa deletada"}), 200