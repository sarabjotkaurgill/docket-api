from rest_framework import serializers

from docket.db.models import UserPermission

# serializers
from docket.api.serializers import BoardDetailSerializer, UserSerializer

class UserPermissionSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = UserPermission
        fields = ('id', 'can_view', 'can_create', 'can_update', 'can_delete')
        