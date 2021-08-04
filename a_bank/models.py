from django.db import models
from datetime import datetime

# Create your models here.
#get User Model
from django.contrib.auth import get_user_model
User = get_user_model()

class Bank(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '1-Bank'

