from django.shortcuts import render
from rest_framework import viewsets
from .serializers  TaskSerializers
from.models import Task

# Create your views here.
class=TaskViewset(viewsets.ModelViewset):
    queryset=Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers
