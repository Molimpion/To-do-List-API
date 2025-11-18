from src.extensions import db
from src.models import Todo
from src.exceptions import ValidationError
from .exceptions import TodoNotFoundError

class TodoService:
    @staticmethod
    def create(user_id, data):
        title = data.get('title')
        
        if not title:
            raise ValidationError("O título é obrigatório.")

        new_todo = Todo(
            title=title,
            description=data.get('description', ''),
            user_id=user_id
        )
        
        db.session.add(new_todo)
        db.session.commit()
        
        return new_todo

    @staticmethod
    def list_all(user_id, page, limit):
        return Todo.query.filter_by(user_id=user_id).paginate(
            page=page, per_page=limit, error_out=False
        )

    @staticmethod
    def delete(user_id, todo_id):
        todo = Todo.query.filter_by(id=todo_id, user_id=user_id).first()
        
        if not todo:
            raise TodoNotFoundError()
        
        db.session.delete(todo)
        db.session.commit()