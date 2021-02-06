from django.contrib import admin
from docket.db.models import (
    Project,
    Board,
    Task,
    BoardTasks,
)

admin.site.site_header = "Docket API"

admin.site.register(Project)
admin.site.register(Board)
admin.site.register(Task)
admin.site.register(BoardTasks)
