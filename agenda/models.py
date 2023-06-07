from django.db import models


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    compromisso = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=200)
    deadline = models.DateField()
    def __str__(self):
        return self.compromisso

   
