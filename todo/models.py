from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    complate = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}-{self.created_date.date()}"

    def show_username(self):
        return f"{self.user.username}"