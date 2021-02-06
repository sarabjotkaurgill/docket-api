from typing import Sequence
from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE

# mixins
from docket.db.mixins import UserTimeAuditModel, TimeAuditModel

# models

from docket.db.models import Task, Project


class BoardTypes(models.IntegerChoices):
    BOARD = 0, "BOARD"
    BACKLOG = 1, "BACKLOG"
    SPRINT = 2, "SPRINT"
    TIMELINE = 3, "TIMELINE"


class Board(UserTimeAuditModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=255, blank=True)
    project = models.ForeignKey(Project, on_delete=CASCADE, related_name="boards")
    board_type = models.IntegerField(
        choices=BoardTypes.choices, default=BoardTypes.BOARD
    )

    def get_board_type_label(self):
        return BoardTypes.labels[self.board_type]


class BoardTasks(TimeAuditModel):
    board = models.ForeignKey(Board, on_delete=CASCADE, related_name="tasks")
    task = models.ForeignKey(Task, on_delete=CASCADE, related_name="boards")
    sequence = models.IntegerField()
