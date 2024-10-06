import simulacao
import os
from pathlib import Path
from rich.console import Console
import typer
from .my_lib import executar_simulacao


app = typer.Typer(no_args_is_help=True)
console = Console()

@app.command('info')
def print_info(custom_message : str = ""):
    """
    Print information about the module
    """
    console.print("Hello! I am simulacao")
    console.print(f"Author: { simulacao.__author__}")
    console.print(f"Version: { simulacao.__version__}")
    if custom_message != "":
        console.print(f"Custom message: {custom_message}")

@app.command() # Defines a default action
def run():
    """
    Probably run the main function of the module
    """
    executar_simulacao()

if __name__ == "__main__":
    app()