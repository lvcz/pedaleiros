from django.db import models


class Ciclistas(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500, null=False)
    sexo = models.CharField(max_length=1)
    data_de_nascimento = models.DateField()
    data_de_inscricao = models.DateTimeField()
    email = models.CharField(max_length=200, null=False)
    senha = models.CharField(max_length=600, null=False)
