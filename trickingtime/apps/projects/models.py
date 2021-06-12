import uuid as uuid_lib
import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

logger = logging.getLogger(__name__)


class Project(models.Model):

    code_name = models.CharField(
        _('Code Name'),
        max_length=10,
        blank=False, null=False,
        unique=True,
        help_text=_("The code name of the Project, e.i. XYZ123"),
    )
    short_description = models.CharField(
        _('Short Description'),
        max_length=69,
        blank=True, null=False,
        help_text=_("A short description for the Project, e.i. Cooking "
                    "Journey"),
    )

    def __str__(self):
        return self.code_name

    def save(self, *args, **kwargs):
        self.code_name = self.code_name.upper()
        super(Project, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
