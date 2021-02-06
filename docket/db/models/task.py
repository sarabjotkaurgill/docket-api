from django.db import models

# mixins
from docket.db.mixins import TimeAuditModel
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# mixins
from docket.db.mixins import TimeAuditModel, UserTimeAuditModel

# models
from .media import Media


class PriorityLabel(models.IntegerChoices):
    DEFAULT = 0, "DEFAULT"
    LOW = 1, "LOW"
    MEDIUM = 2, "MEDIUM"
    HIGH = 3, "HIGH"


class Task(UserTimeAuditModel):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)
    due_date = models.DateTimeField(null=True)
    priority = models.IntegerField(
        choices=PriorityLabel.choices, default=PriorityLabel.DEFAULT
    )
    is_checked = models.BooleanField(default=False)
    remind_me = models.DateField(null=True)

    def get_priority_label(self):
        return PriorityLabel.labels[self.priority]


class TaskAssignee(TimeAuditModel):
    task = models.ForeignKey(Task, on_delete=CASCADE, related_name="assignees")
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="assignees")


class SubTask(TimeAuditModel):
    task = models.ForeignKey(Task, on_delete=CASCADE, related_name="subtasks")
    name = models.CharField(max_length=256)
    is_checked = models.BooleanField(default=False)


class TaskMedia(TimeAuditModel):
    task = models.ForeignKey(Task, on_delete=CASCADE, related_name="medias")
    media = models.ForeignKey(Media, on_delete=CASCADE, related_name="medias")


class TaskCommentKind(models.IntegerChoices):
    HUMAN = 0, "HUMAN"
    BOT = 1, "BOT"
    ACTION = 2, "ACTION"


class TaskComment(TimeAuditModel):
    user = models.ForeignKey(User, null=True, on_delete=CASCADE)
    task = models.ForeignKey(Task, on_delete=CASCADE, related_name="comments")
    content = models.TextField()
    kind = models.IntegerField(
        choices=TaskCommentKind.choices, default=TaskCommentKind.HUMAN
    )
