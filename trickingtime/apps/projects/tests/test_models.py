from django.test import TestCase
from django.core.exceptions import ValidationError

from faker import Faker
from faker_airtravel import AirTravelProvider

from projects.models import (
    Project
)

fake = Faker()
fake.add_provider(AirTravelProvider)


class ProjectTestCase(TestCase):
    def setUp(self):
        self.code_name = fake.airport_icao().title()

        self.project = Project.objects.create(
            code_name=self.code_name,
            short_description=fake.text(max_nb_chars=60)
        )

    def test_entries(self):
        self.assertEqual(self.project.code_name, self.code_name.upper())

    def test__str__(self):
        self.assertEqual(self.project.__str__(), self.project.code_name)
