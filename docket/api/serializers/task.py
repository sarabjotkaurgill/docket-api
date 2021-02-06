from rest_framework import serializers

# models
from docket.db.models import Task, SubTask, TaskComment

# serializers
from .accounts import UserSerializer


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = "__all__"


class TaskCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TaskComment
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    comments = TaskCommentSerializer(many=True, read_only=True)
    sub_tasks = SubTaskSerializer(many=True, read_only=True)
    priority = serializers.CharField(source="get_priority_label", read_only=True)

    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "description",
            "due_date",
            "remind_me",
            "priority",
            "is_checked",
            "comments",
            "sub_tasks",
            "created_by",
        )
