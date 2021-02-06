from django.db.models.enums import Choices
from rest_framework import serializers

# models
from docket.db.models import Project, DisplayTypes

# serializers
from docket.api.serializers import BoardDetailSerializer, UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


class ProjectDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    boards = BoardDetailSerializer(many=True, read_only=True)
    display_type = serializers.CharField(source="get_display_type_name", read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
