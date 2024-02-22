from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name.username} -- {self.book.title}'