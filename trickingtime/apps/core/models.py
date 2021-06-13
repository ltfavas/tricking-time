import uuid as uuid_lib
import logging

from django.db import models

logger = logging.getLogger(__name__)
# Create your models here.


class UUIDModel(models.Model):
    uuid = models.UUIDField(
        editable=False,
        db_index=True,
        default=uuid_lib.uuid4,
    )

    class Meta:
        abstract = True
