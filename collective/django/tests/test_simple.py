import unittest2 as unittest
import transaction

from layers import DJANGO_LAYER
from dummypackage.models import Person


class TestSimple(unittest.TestCase):
    layer = DJANGO_LAYER

    def test_commit(self):
        montys = [
            Person(
                first_name = "Eric",
                last_name = "Idle"
            ),
            Person(
                first_name = "Michael",
                last_name = "Palin"
            ),
            Person(
                first_name = "Graham",
                last_name = "Chapman"
            ),
            Person(
                first_name = "Terry",
                last_name = "Jones"
            ),
            Person(
                first_name = "Terry",
                last_name = "Gilliam"
            ),
            Person(
                first_name = "John",
                last_name = "Cleese"
            )
        ]
        for monty in montys:
            monty.save()
        transaction.commit()
        self.assertItemsEqual(
            ["Eric", "Michael", "Graham", "Terry", "Terry", "John"],
            [ m.first_name for m in Person.objects.all() ]
        )

    def test_abort(self):
        montys = [
            Person(
                first_name = "Eric",
                last_name = "Idle"
            ),
            Person(
                first_name = "Michael",
                last_name = "Palin"
            ),
            Person(
                first_name = "Graham",
                last_name = "Chapman"
            ),
            Person(
                first_name = "Terry",
                last_name = "Jones"
            ),
            Person(
                first_name = "Terry",
                last_name = "Gilliam"
            ),
            Person(
                first_name = "John",
                last_name = "Cleese"
            )
        ]
        for monty in montys:
            monty.save()
        transaction.abort()
        self.assertEqual(0, Person.objects.count())
