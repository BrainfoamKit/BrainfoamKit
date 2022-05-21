"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Brainfoamkit."""


if __name__ == "__main__":
    main(prog_name="BrainfoamKit")  # pragma: no cover
