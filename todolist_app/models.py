from django.conf import settings
from django.db import models


class Priority(models.Model):

    name = models.CharField(max_length=20)
    orders = models.IntegerField()


class Todo(models.Model):

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    assigned_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='assigned',)
    done = models.BooleanField(default=False)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='created',)
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='updated',)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE,)
