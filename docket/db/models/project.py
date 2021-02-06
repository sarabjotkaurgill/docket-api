from django.db import models
from django.contrib.auth.models import User

# mixins
from docket.db.mixins import UserTimeAuditModel


class DisplayTypes(models.IntegerChoices):
    KANBAN = 0, "KANBAN"
    LIST = 1, "LIST"


class Project(UserTimeAuditModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=10, blank=True)
    color = models.CharField(max_length=10, blank=True)
    display_type = models.IntegerField(
        choices=DisplayTypes.choices, default=DisplayTypes.KANBAN
    )

    def get_display_type_name(self):
        return DisplayTypes.labels[self.display_type]