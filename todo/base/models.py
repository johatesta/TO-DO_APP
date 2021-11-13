from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'


class Folder(models.Model):
    title= models.TextField(max_length=120)
    items=ForeignKey(Task,on_delete=CASCADE,verbose_name='Task')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)