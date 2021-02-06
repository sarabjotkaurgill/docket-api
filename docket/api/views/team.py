from django.shortcuts import get_object_or_404
from django.http import Http404

# drf
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# serializers
from docket.api.serializers import TeamSerializer

# models
from docket.db.models import Team, Board

class TeamViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

    # def retrieve(self, request, pk=None):
    #     queryset = Board.objects.all()
    #     project = get_object_or_404(queryset, pk=pk)
    #     serializer = TeamSerializer(project)
    #     return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = TeamSerializer(data=request.data)
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

    # def get_object(self, pk):
    #     try:
    #         return Board.objects.get(pk=pk)
    #     except Board.DoesNotExist:
    #         raise Http404