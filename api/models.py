from django.db import models

# Create your models here.
# Modelo de dados

# Para este sistema de gerenciamento de tarefas, a entidade "tarefa" deve ter os seguintes atributos:

#     Identificador: código que identifica de forma única a tarefa.
#     Descrição: informação textual que descreve a tarefa.
#     Prazo: data/hora que informa o limite para completar a tarefa.
#     Completa: valor lógico que define se a tarefa já foi completada.


class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField(max_length=390)
    prazo = models.DateTimeField()
    completa = models.BooleanField(default=False)