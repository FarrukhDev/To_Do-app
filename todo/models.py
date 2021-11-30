from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(max_length=10,choices=(('new','new'),('done','done')))
    date = models.DateTimeField(default=timezone.now)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title