from django.core.management.base import BaseCommand
from candidates.models import Ballot


class Command(BaseCommand):

    help = """
    Find and mark any uncontested ballots not already marked after ballot lock
    """

    def handle(self, *args):
        qs = Ballot.objects.uncontested()
        for ballot in qs:
            ballot.mark_uncontested_winners()
