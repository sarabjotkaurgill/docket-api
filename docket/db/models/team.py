from django.db import models
from django.contrib.auth.models import User

# mixins
from docket.db.mixins import UserTimeAuditModel
from django.db.models.deletion import CASCADE

# models
from docket.db.models import UserPermission


class Team(UserTimeAuditModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="team1")
    user_permission = models.ForeignKey(
        UserPermission, on_delete=CASCADE, related_name="team"
    )
