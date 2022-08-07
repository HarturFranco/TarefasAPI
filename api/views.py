from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TarefaSerializer
from .models import Tarefa

# Create your views here.

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = (TarefaSerializer)
