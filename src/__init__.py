from flask import Flask, jsonify
from dotenv import load_dotenv
from flasgger import Swagger
import os
import logging
from rich.logging import RichHandler
from src.extensions import db, jwt
from src.modules.auth import auth_bp
from src.modules.todos import todos_bp
from src.exceptions import APIError

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    app.config['SWAGGER'] = {
        'title': 'Todo List API',
        'uiversion': 3,
        "specs_route": "/docs"
    }
    
    swagger_template = {
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: \"Bearer {token}\""
            }
        },
        "security": [
            {"Bearer": []}
        ]
    }

    db.init_app(app)
    jwt.init_app(app)
    Swagger(app, template=swagger_template)

    @app.errorhandler(APIError)
    def handle_api_error(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @app.errorhandler(404)
    def handle_404(error):
        return jsonify({"error": True, "message": "Endpoint não encontrado"}), 404

    @app.errorhandler(500)
    def handle_500(error):
        return jsonify({"error": True, "message": "Erro interno"}), 500

    @jwt.expired_token_loader
    def expired_token(jwt_header, jwt_payload):
        return jsonify({"error": True, "message": "Token expirado"}), 401

    @jwt.invalid_token_loader
    def invalid_token(error):
        return jsonify({"error": True, "message": "Token inválido"}), 401

    @jwt.unauthorized_loader
    def missing_token(error):
        return jsonify({"error": True, "message": "Token ausente"}), 401

    app.register_blueprint(auth_bp)
    app.register_blueprint(todos_bp)

    with app.app_context():
        db.create_all()

    return app