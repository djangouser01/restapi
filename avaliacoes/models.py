from django.db import models
from django.contrib.auth.models import User


class Avaliacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(decimal_places=4, max_digits=6)
    data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username + " - " + str(self.nota)


