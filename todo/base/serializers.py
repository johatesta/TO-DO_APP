from django.db.models import fields
from rest_framework import serializers
from .models import Task , listofTask
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'

class ListofTaskSerializer(serializers.ModelSerializer):
	class Meta:
		model= listofTask
		fields='__all__'