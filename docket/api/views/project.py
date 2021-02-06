from django.shortcuts import get_object_or_404
from django.http import Http404

# drf
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# serializers
from docket.api.serializers import ProjectSerializer, ProjectDetailSerializer

# models
from docket.db.models import Project


class ProjectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Project.objects.filter(created_by=request.user)
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # request.data["user"] = request.user
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

    def retrieve(self, request, pk=None):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

    def destroy(self, request, pk=None):
        try:
            project = self.get_object(pk)
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404
            