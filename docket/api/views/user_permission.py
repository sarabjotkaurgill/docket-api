from docket.db.models import user_permission
from django.http import Http404

# drf
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# serializers
from docket.api.serializers import UserPermissionSerializer

# models
from docket.db.models import UserPermission


class UserPermissionViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        serializer = UserPermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user_permission)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
