from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import TarefaViewSet

router = routers.DefaultRouter()
router.register('tarefas', TarefaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]