
from django.conf import settings
from django.db import models
from django.utils import timezone


class post(models.Model):
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    text = models.TextField()
    data_de_criacao = models.DateTimeField(default=timezone.now)
    data_de_publicacao = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.data_de_publicacao = timezone.now()
        self.save()


    def __str__(self):
        return self.titulo