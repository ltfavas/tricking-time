import uuid as uuid_lib
import logging
from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from .helpers import (
    generate_slug,
    get_duration,
    get_duration_decimal
)
from projects.models import Project

logger = logging.getLogger(__name__)


class WorkDay(models.Model):

    day = models.DateField(
        _('Day'),
        editable=False,
    )

    slug = models.SlugField(
        unique=True,
        editable=False,
        max_length=50,
        null=False, blank=False,
    )

    @property
    def get_work_entries(self):
        return self.work_entries.all()

    def save(self, *args, **kwargs):
        self.day = date.today()
        self.slug = generate_slug(self.day)
        super(WorkDay, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = _("Work Day")
        verbose_name_plural = _("Work Days")


class WorkEntry(models.Model):

    day = models.ForeignKey(
        WorkDay,
        null=True,
        on_delete=models.SET_NULL,
        related_name="work_entries"
    )

    begin_time = models.TimeField(
        _('Begin'),
        blank=False, null=False,
        help_text=_("The hour and minutes in which the activity was started")
    )

    end_time = models.TimeField(
        _('End'),
        blank=True, null=True,
        help_text=_("The hour and minutes in which the activity was ended")
    )

    duration = models.TimeField(
        _('Duration'),
        null=True,
        editable=False,
        help_text=_("The duration of time between begin and end")
    )

    duration_decimal = models.DecimalField(
        _('Duration in Decimal'),
        max_digits=3,
        decimal_places=2,
        null=True,
        editable=False,
        help_text=_(
            "The duration of time between begin and end in decimal hours")
    )

    description = models.CharField(
        _('Description'),
        max_length=200,
        blank=False, null=False,
        help_text=_("A description for the activity Cooking, e.i Making Soup "
                    "with Mrs. Lovett"),
    )

    project = models.ForeignKey(
        Project,
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )

    def save(self, *args, **kwargs):
        if not self.end_time:
            return super(WorkEntry, self).save(*args, **kwargs)

        self.duration = get_duration(
            start_time=self.begin_time,
            end_time=self.end_time
        )
        self.duration_decimal = get_duration_decimal(
            time_var=self.duration
        )

        super(WorkEntry, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Work Entry")
        verbose_name_plural = _("Work Entries")
