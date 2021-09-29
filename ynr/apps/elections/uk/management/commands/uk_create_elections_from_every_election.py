from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models.functions import Greatest
from django.utils import timezone
from dateutil.parser import parse

from candidates.models import Ballot
from elections.models import Election
from elections.uk.every_election import EveryElectionImporter


class Command(BaseCommand):
    help = "Create posts and elections from a EveryElection"

    def add_arguments(self, parser):
        parser.add_argument(
            "--full",
            action="store_true",
            help="Do a full import of all elections",
        )
        parser.add_argument(
            "--poll-open-date",
            action="store",
            type=self.valid_date,
            help="Just import elections for polls that open on a given date",
        )
        parser.add_argument(
            "--recently-updated",
            dest="recently_updated",
            action="store_true",
            help="Only import elections that have been updated since last ee_modified date",
        )

    def valid_date(self, value):
        return parse(value).date()

    def get_latest_ee_modified_datetime(self):
        """
        Returns a timestamp of the last known update to an Election in
        EveryElection that has been stored against a Ballot or
        Election in our database.
        """
        ballots = Ballot.objects.annotate(
            latest_ee_modified=Greatest("ee_modified", "election__ee_modified")
        )
        return ballots.latest("latest_ee_modified").latest_ee_modified

    def default_timestamp(self):
        """
        Returns a timestamp set to before the 'modified' timestamp was
        added to the Election model in EveryElection.
        """
        return timezone.datetime(2021, 9, 1, tzinfo=timezone.utc)

    def import_approved_elections(
        self, full=False, poll_open_date=None, recently_updated=False
    ):
        # Get all approved elections from EveryElection
        query_args = None
        if full:
            query_args = {}
        if poll_open_date:
            query_args = {"poll_open_date": poll_open_date}

        if recently_updated:
            timestamp = (
                self.get_latest_ee_modified_datetime()
                or self.default_timestamp()
            )
            query_args = {"modified": timestamp.isoformat()}

        ee_importer = EveryElectionImporter(query_args)
        ee_importer.build_election_tree()

        for ballot_id, election_dict in ee_importer.ballot_ids.items():
            parent = ee_importer.get_parent(ballot_id)
            election_dict.get_or_create_ballot(parent=parent)

    def delete_deleted_elections(self):
        # Get all deleted elections from EE
        ee_importer = EveryElectionImporter(
            {
                "poll_open_date__gte": str(date.today() - timedelta(days=30)),
                "deleted": 1,
            }
        )
        ee_importer.build_election_tree()

        for ballot_id, election_dict in ee_importer.ballot_ids.items():
            election_dict.delete_ballot()

        for group_id, election_dict in ee_importer.group_ids.items():
            election_dict.delete_election()

    def handle(self, *args, **options):
        current_only = not any(
            (
                options["full"],
                options["poll_open_date"],
                options["recently_updated"],
            )
        )
        with transaction.atomic():
            if current_only:
                # Mark all elections as not current, any that are current will
                # be (re)set later
                Election.objects.update(current=False)

            self.import_approved_elections(
                full=options["full"],
                poll_open_date=options["poll_open_date"],
                recently_updated=options["recently_updated"],
            )
            self.delete_deleted_elections()
