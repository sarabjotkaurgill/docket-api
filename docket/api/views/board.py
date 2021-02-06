from django.shortcuts import get_object_or_404
from django.http import Http404

# drf
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# serializers
from docket.api.serializers import BoardSerializer, BoardTaskSerializer, TaskSerializer

# models
from docket.db.models import Board


class BoardTaskViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request, pk):
        task_serializer = TaskSerializer(data=request.data)
        if task_serializer.is_valid():
            task_serializer.save(created_by=request.user)
            board_task_data = {
                "board": pk,
                "task": task_serializer.data["id"],
                "sequence": 0,
            }
            print(board_task_data)
            board_task_serializer = BoardTaskSerializer(data=board_task_data)
            if board_task_serializer.is_valid():
                board_task_serializer.save()
                return Response(
                    board_task_serializer.data, status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    board_task_serializer.errors,
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                )
        else:
            return Response(
                task_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

    def update(self, request, pk):
        task_serializer = TaskSerializer(data=request.data)
        if task_serializer.is_valid():
            task_serializer.save(created_by=request.user)
            board_task_data = {
                "board_id": pk,
                "task_id": task_serializer.data["id"],
                "sequence": 0,
            }
            board_task_serializer = BoardTaskSerializer(data=board_task_data)
            if board_task_serializer.is_valid():
                board_task_serializer.save()
                return Response(
                    board_task_serializer.data, status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    board_task_serializer.errors,
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                )
        else:
            return Response(
                task_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )


class BoardViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

    def retrieve(self, request, pk=None):
        queryset = Board.objects.all()
        board = get_object_or_404(queryset, pk=pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Board.objects.all()
        board = get_object_or_404(queryset, pk=pk)
        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

    def destroy(self, request, pk=None):
        try:
            board = self.get_object(pk)
            board.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Http404