from rest_framework import serializers

# models
from docket.db.models import Board, BoardTasks

# serializers
from .task import TaskSerializer


class BoardTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardTasks
        fields = ("sequence", "board", "task")


class BoardSerializer(serializers.ModelSerializer):
    board_type = serializers.CharField(source="get_board_type_label", read_only=True)

    class Meta:
        model = Board
        fields = ("id", "name", "description", "icon", "board_type", "project")


class BoardTaskReadOnlySerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)
    board = BoardSerializer(read_only=True)

    class Meta:
        model = BoardTasks
        fields = ("sequence", "board", "task", "id")


class BoardDetailSerializer(serializers.ModelSerializer):
    board_type = serializers.CharField(source="get_board_type_label", read_only=True)
    tasks = BoardTaskReadOnlySerializer(many=True)

    class Meta:
        model = Board
        fields = ("id", "name", "description", "icon", "board_type", "project", "tasks")