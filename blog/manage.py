import click
from flask.cli import FlaskGroup

from blog.app import create_app


def create_blog(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_blog)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    from blog.extensions import db
    from blog.models import Post
    click.echo("create database")
    db.create_all()
    click.echo("done")

    click.echo("create post")
    post = Post(
        title='init post',
        content='init post content'
    )
    db.session.add(post)
    db.session.commit()
    click.echo("created initial post")

if __name__ == "__main__":
    cli()
