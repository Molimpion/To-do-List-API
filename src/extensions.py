from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Instanciamos aqui, mas só iniciamos no __init__.py principal
db = SQLAlchemy()
jwt = JWTManager()