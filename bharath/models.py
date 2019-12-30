from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.phone}, {self.message}"
