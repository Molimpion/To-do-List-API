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
    def update(user_id, todo_id, data):
        todo = Todo.query.filter_by(id=todo_id, user_id=user_id).first()
        
        if not todo:
            raise TodoNotFoundError()

        # Atualiza apenas se o campo foi enviado no JSON (preserva o valor antigo caso contrário)
        todo.title = data.get('title', todo.title)
        todo.description = data.get('description', todo.description)
        
        # Verificação específica para booleano (porque False é um valor válido)
        if 'is_completed' in data:
            todo.is_completed = data['is_completed']

        db.session.commit()
        return todo

    @staticmethod
    def list_all(user_id, page, limit, status=None):
        # Começa filtrando apenas as tarefas do usuário
        query = Todo.query.filter_by(user_id=user_id)

        # Aplica filtro de status se for passado
        if status == 'completed':
            query = query.filter_by(is_completed=True)
        elif status == 'pending':
            query = query.filter_by(is_completed=False)

        # Retorna ordenado pelas mais recentes primeiro
        return query.order_by(Todo.created_at.desc()).paginate(
            page=page, per_page=limit, error_out=False
        )

    @staticmethod
    def delete(user_id, todo_id):
        todo = Todo.query.filter_by(id=todo_id, user_id=user_id).first()
        
        if not todo:
            raise TodoNotFoundError()
        
        db.session.delete(todo)
        db.session.commit()