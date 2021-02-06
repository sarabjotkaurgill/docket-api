from django.db import models

# mixins
from docket.db.mixins import UserTimeAuditModel


class UserPermission(UserTimeAuditModel):
    can_view = models.BooleanField(default=True)
    can_create = models.BooleanField(default=True)
    can_update = models.BooleanField(default=True)
    can_delete = models.BooleanField(default=True)