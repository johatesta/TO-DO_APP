from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets,status, permissions
from .serializers import TodoSerializer  # add this
from .models import Todo
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer  # add this
    queryset = Todo.objects.all()
    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response("No tiene permisos suficientes", status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("No tiene permisos suficientes", status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response("No tiene permisos suficientes", status=status.HTTP_400_BAD_REQUEST)

