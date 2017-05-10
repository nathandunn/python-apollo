import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('get_sequences')
@click.argument("organism_id", type=str)


@pass_context
@apollo_exception
@dict_output
def cli(ctx, organism_id):
    """Get the sequences for an organism
    """
    return ctx.gi.organisms.get_sequences(organism_id)