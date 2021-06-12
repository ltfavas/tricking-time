from datetime import datetime, date, time
from decimal import Decimal

from django.test import TestCase
from django.core.exceptions import ValidationError

from work_time.models import (
    WorkDay,
    WorkEntry
)


class WorDayTestCase(TestCase):
    def setUp(self):
        self.work_day = WorkDay.objects.create()

    def test_slug(self):
        self.assertEqual(self.work_day.slug, date.today().strftime("%d-%m-%Y"))

    def test_entries(self):
        self.assertEqual(self.work_day.get_work_entries.count(), 0)

    def test__str__(self):
        self.assertEqual(self.work_day.__str__(), self.work_day.slug)


class WorkEntryTestCase(TestCase):
    def setUp(self):
        self.work_day = WorkDay.objects.first()

    def test_can_create_without_end_time(self):

        try:
            entry = WorkEntry.objects.create(
                day=self.work_day,
                begin_time=time(
                    hour=1,
                    minute=1,
                    second=1
                ),
                description="big description",
            )
        except Exception:
            self.fail("Unable to create WorkEntry without end_time field")

    def test_calculate_duration(self):

        entry = WorkEntry.objects.create(
            day=self.work_day,
            begin_time=time(
                hour=1,
                minute=0,
                second=0
            ),
            end_time=time(
                hour=2,
                minute=30,
                second=0
            ),
            description="big description",
        )

        self.assertEqual(entry.duration, time(hour=1, minute=30))

    def test_calculate_duration_in_decimal(self):

        entry = WorkEntry.objects.create(
            day=self.work_day,
            begin_time=time(
                hour=1,
                minute=0,
                second=0
            ),
            end_time=time(
                hour=2,
                minute=30,
                second=0
            ),
            description="big description",
        )

        self.assertEqual(entry.duration_decimal, Decimal("1.5"))

        entry2 = WorkEntry.objects.create(
            day=self.work_day,
            begin_time=time(
                hour=0,
                minute=0,
                second=0
            ),
            end_time=time(
                hour=0,
                minute=5,
                second=0
            ),
            description="big description",
        )
        # should be 0,083333333
        self.assertEqual(round(entry2.duration_decimal, 2), Decimal("0.08"))

        entry3 = WorkEntry.objects.create(
            day=self.work_day,
            begin_time=time(
                hour=0,
                minute=0,
                second=0
            ),
            end_time=time(
                hour=0,
                minute=10,
                second=0
            ),
            description="big description",
        )
        # should be 0,166666667
        self.assertEqual(round(entry3.duration_decimal, 2), Decimal("0.17"))
