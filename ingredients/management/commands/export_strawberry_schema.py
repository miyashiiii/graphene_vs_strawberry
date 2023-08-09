from django.core.management import BaseCommand
from strawberry.printer import print_schema

from ingredients.schema_strawberry import schema


class Command(BaseCommand):
    """Export the strawberry schema to a file
    Because strawberry doesn't have a command to export the schema to a file,
    we need to create one ourselves.
    See https://github.com/strawberry-graphql/strawberry/issues/1583#issuecomment-1132720229
    """

    help = "Exports the strawberry graphql schema"

    def handle(self, *args, **options):
        print(print_schema(schema))
