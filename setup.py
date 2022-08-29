import click

@click.command()
@click.option('--name')

def main(name):
    fname = click.prompt("Enter your first name")
    click.echo(f"Your name is {fname}")

if __name__ == '__main__':
    main()
