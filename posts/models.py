from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    
    # Agregado valor por defecto para evitar errores en migraciones
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        default=1  # Cambia el ID si es necesario
    )
    
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        default=1  # Cambia el ID si es necesario
    )
    
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])  # Se usará para detalles de publicaciones
