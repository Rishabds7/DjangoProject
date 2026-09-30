from django.db import models

# Create your models here.

class UserDetails(models.Model):
    username = models.CharField(max_length=150, primary_key = True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.username} - {self.email}"
