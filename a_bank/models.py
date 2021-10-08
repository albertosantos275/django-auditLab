from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
import uuid
import os
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
    class BatchStatus(models.TextChoices):
        PENDING = 'pending', _('Pending')
        PROCESSING = 'processing', _('Processing')
        DONE = 'Done', _('Done')
    bank_id = models.ForeignKey(Bank,related_name='batch_bank',on_delete=models.CASCADE,unique=False,blank=False,null=False)
    status = models.CharField(max_length=30, choices= BatchStatus.choices,default=BatchStatus.PENDING)
    store_path = models.CharField(max_length=200, blank=True)
    processed_time = models.DateTimeField(default=datetime.now, blank=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.bank_id.name+ '--' +self.status + "--" + str(self.bank_id.id)
    class Meta:
        verbose_name = '2-Batch'


class FileTypes(models.Model):    
    name = models.CharField(max_length=100, blank=False, unique=True)
    code = models.CharField(max_length=20, blank=True, unique=False)
    create_on = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name + ' -- ' +  self.code
    class Meta:
        verbose_name = '3-File Type'


def get_file_path(instance, filename):
    print(instance, filename)
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(instance.batch_id.bank_id.name + '/' +instance.file_type_id.name, filename)

class File(models.Model):
    batch_id = models.ForeignKey(Batch,related_name='file_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
    file_type_id = models.ForeignKey(FileTypes,related_name='file_type_files',on_delete=models.CASCADE,unique=False,blank=True,null=True)
    file_url = models.FileField('Document', upload_to = get_file_path, blank=True,null=True)
    file_name  = models.CharField(max_length=100, blank=True, unique=False, )
    create_on = models.DateTimeField(default=datetime.now, blank=True, )
    def __str__(self):
        return self.file_name
    class Meta:
        verbose_name = '4-File'



