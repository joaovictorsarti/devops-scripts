import typer
import os 
app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def upchart(name: str, upgrade: bool = False):
    if upgrade:
         os.system(f"echo Uploading MS {name}. Happy helms :p")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
