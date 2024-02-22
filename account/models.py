from django.db import models
from django.contrib.auth.models import User
from book.models import Book

# Create your models here.


class UserAccount(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="account")
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class BorrowHistory(models.Model):
    account = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name="account")
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="book")
    posted_on = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.book}'
