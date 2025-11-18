from src.exceptions import APIError

class TodoNotFoundError(APIError):
    def __init__(self, message="Tarefa não encontrada"):
        super().__init__(message, status_code=404)