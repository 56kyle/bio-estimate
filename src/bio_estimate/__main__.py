"""Command-line interface."""

import typer


app: typer.Typer = typer.Typer()


@app.command(name="bio-estimate")
def main() -> None:
    """Bio Estimate."""


if __name__ == "__main__":
    app()  # pragma: no cover
