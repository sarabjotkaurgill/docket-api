from rest_framework import serializers

from docket.db.models import Team

# serializers
from docket.api.serializers import BoardDetailSerializer, UserSerializer

class TeamSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Team
        fields = "__all__"
        