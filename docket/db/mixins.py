from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE


class UserTimeAuditModel(models.Model):
    """
    To path when the record was created, last modified and who created
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Modified At")
    created_by = models.ForeignKey(User, on_delete=CASCADE)

    class Meta:
        abstract = True


class TimeAuditModel(models.Model):
    """
    To path when the record was created and last modified
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Modified At")

    class Meta:
        abstract = True