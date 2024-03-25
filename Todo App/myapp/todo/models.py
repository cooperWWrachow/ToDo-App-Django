from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.

class Task(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['due_date']