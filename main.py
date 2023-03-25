# Importamos las librerias
import openai
import config  # modulo donde esta la api_key
import typer
from rich import print
from rich.table import Table


def main():
    # configuramos la api_key
    openai.api_key = config.api_key

    print("🤖 [bold green]ChatGPT API con Python[/bold green]")

    table = Table("Comandos", "Descripcion")
    table.add_row("salir", "Salir de la aplicacion")
    table.add_row("nuevo", "Crear una nueva conversacion")

    print(table)

    # Contexto del sistema
    context = {"role": "system", "content": "Eres un asistente de programacion"}

    # definimos la variable
    messages = [context]

    while True:
        # definimos el mensaje
        content = __prompt()

        if content == "nuevo":
            print("🆕 Nueva Conversacion")
            messages = [context]
            content = __prompt()

        # definimos el rol de usuario
        messages.append({"role": "user", "content": content})

        # definimos la respuesta
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

        # definimos la variable respuesta
        respuesta_contenido = response.choices[0].message.content

        # definimos el rol de asistente y guardara las respuestas
        messages.append({"role": "assistant", "content": respuesta_contenido})

        # Se imprime la respuesta
        print(f'[bold green]> [/bold green] [green]{respuesta_contenido}[/green]')


def __prompt() -> str:
    # definimos el mensaje
    prompt = typer.prompt("\n¿Sobre que quieres hablar? ")

    if prompt == "salir":
        salir = typer.confirm("🤚 ¿Realmente quieres salir?")
        if salir:
            print('👋 ¡Hasta luego!')
            raise typer.Abort()
        return __prompt()
    
    return prompt

if __name__ == "__main__":
    typer.run(main)
