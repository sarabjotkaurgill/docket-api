from django.db import models
from django.contrib.auth.models import User

# mixins
from docket.db.mixins import TimeAuditModel


class Media(TimeAuditModel):
    name = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    is_private = models.BooleanField(default=True)