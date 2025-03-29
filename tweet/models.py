from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Serve para salvar ela 350 por 350 antes no banco de dados
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Salva a imagem original

        if self.photo:
            img = Image.open(self.photo.path)

            # Redimensiona a imagem para 350x350 mantendo a proporção
            img.thumbnail((350, 350))

            # Salva a imagem redimensionada
            img.save(self.photo.path)
