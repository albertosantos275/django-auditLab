from django.db import models
from datetime import datetime

from django.contrib.auth import get_user_model
User = get_user_model()

class Bank(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '1-Bank'



class Batch(models.Model):
    status = models.CharField(max_length=100, blank=False, unique=True)
    bank_id = models.ForeignKey(Bank,related_name='batch_bank',on_delete=models.CASCADE,unique=False,blank=False,null=False)
    store_path = models.CharField(max_length=200, blank=True)
    processed_time = models.DateTimeField(default=datetime.now, blank=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.status + "--" + self.bank_id
    class Meta:
        verbose_name = '2-Batch'


class File(models.Model):
    batch_id = models.ForeignKey(Batch,related_name='file_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
    file_type = models.CharField(max_length=100, blank=False, unique=True)
    name = models.CharField(max_length=100, blank=False, unique=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '3-File'