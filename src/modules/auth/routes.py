from flask import Blueprint, request, jsonify
from .services import AuthService
from flasgger import swag_from

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Registrar um novo usuário
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: usuario_teste
            password:
              type: string
              example: senha123
    responses:
      201:
        description: Usuário criado com sucesso
      400:
        description: Dados inválidos ou usuário já existe
    """
    data = request.get_json()
    AuthService.register(data)
    return jsonify({"msg": "Usuário criado com sucesso"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Autenticar e receber Token JWT
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: usuario_teste
            password:
              type: string
              example: senha123
    responses:
      200:
        description: Login realizado com sucesso
        schema:
          type: object
          properties:
            access_token:
              type: string
      401:
        description: Credenciais inválidas
    """
    data = request.get_json()
    result = AuthService.login(data)
    return jsonify(result), 200