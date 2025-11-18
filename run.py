from src import create_app
from rich.console import Console

app = create_app()

if __name__ == '__main__':
    console = Console()
    console.rule("[bold yellow]Todo List API[/bold yellow]")
    console.print("\n[bold green] Documentação:[/bold green] [link=http://127.0.0.1:5000/docs]http://127.0.0.1:5000/docs[/link]\n")

    app.run(host='0.0.0.0', port=5000, debug=True)