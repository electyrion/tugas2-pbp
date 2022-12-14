from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    # on_delete=models.CASCADE means that if a user is deleted, all of their tasks will be deleted as well
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)  # tanggal dibuat
    title = models.CharField(max_length=100)  # judul task
    description = models.TextField()  # deskripsi task
    is_finished = models.BooleanField(default=False)  # status task
