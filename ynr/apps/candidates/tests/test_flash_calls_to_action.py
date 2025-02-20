import re

from django.test import TestCase

import people.tests.factories
from candidates.views.people import get_call_to_action_flash_message

from . import factories
from .uk_examples import UK2015ExamplesMixin


def normalize_whitespace(s):
    return re.sub(r"(?ms)\s+", " ", s)


class TestGetFlashMessage(UK2015ExamplesMixin, TestCase):

    maxDiff = None

    def setUp(self):
        super().setUp()
        self.fake_person = people.tests.factories.PersonFactory.create(
            name="Wreck-it-Ralph", id=42
        )
        post_in_2010 = self.edinburgh_east_post
        post_in_2015 = self.edinburgh_north_post
        factories.MembershipFactory.create(
            person=self.fake_person,
            post=post_in_2010,
            ballot=self.edinburgh_east_post_ballot,
            party=self.labour_party,
        )
        factories.MembershipFactory.create(
            person=self.fake_person,
            post=post_in_2015,
            ballot=self.edinburgh_north_post_ballot,
            party=self.labour_party,
        )

    def test_get_flash_message_new_person(self):
        self.assertEqual(
            ' Thank-you for adding <a href="/person/42">Wreck-it-Ralph</a>! '
            "Now you can carry on to:"
            ' <ul> <li> <a href="/person/42/update">Edit Wreck-it-Ralph again</a> </li>'
            ' <li> Add a candidate for <a href="/numbers/attention-needed">one '
            "of the posts with fewest candidates</a> </li>"
            ' <li> <a href="/election/parl.14419.2015-05-07/person/create/">Add another'
            " candidate in the Member of Parliament for Edinburgh East</a> </li> <li> "
            '<a href="/election/parl.14420.2015-05-07/person/create/">Add another candidate '
            "in the Member of Parliament for Edinburgh North and Leith</a> "
            "</li> </ul> ",
            normalize_whitespace(
                get_call_to_action_flash_message(
                    self.fake_person, new_person=True
                )
            ),
        )

    def test_get_flash_message_updated_person(self):
        self.maxDiff = None
        self.assertEqual(
            ' Thank-you for updating <a href="/person/42">Wreck-it-Ralph</a>! '
            'Now you can carry on to: <ul> <li> <a href="/person/42/update">Edit '
            "Wreck-it-Ralph again</a> </li> <li> Add a candidate for "
            '<a href="/numbers/attention-needed">one of the posts with fewest candidates</a> '
            '</li> <li> <a href="/election/parl.14419.2015-05-07/person/create/">Add '
            "another candidate in the Member of Parliament for Edinburgh East</a> </li> "
            '<li> <a href="/election/parl.14420.2015-05-07/person/create/">Add another '
            "candidate in the Member of Parliament for Edinburgh North and Leith</a> "
            "</li> </ul> ",
            normalize_whitespace(
                get_call_to_action_flash_message(
                    self.fake_person, new_person=False
                )
            ),
        )
