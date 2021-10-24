from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
import uuid
import os
from pathlib import Path
from django.db.models import signals
from django.contrib.auth import get_user_model
User = get_user_model()

class Bank(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '1-Bank'

class FileTypes(models.Model):
    class FileSubmittedPeriod(models.TextChoices):
        DAILY = 'daily', _('Daily')
        WEEKLY = 'weekly', _('Weekly')
        MOTHLY = 'monthly', _('Monthly') 
        QUATERLY = 'quaterly', _('Quaterly')   
        BIANNUAL = 'biannual', _('Biannual')  

    name = models.CharField(max_length=100, blank=False, unique=True)
    code = models.CharField(max_length=20, blank=True, unique=False)
    period = models.CharField(max_length=30, choices= FileSubmittedPeriod.choices,default='')

    create_on = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name + ' -- ' +  self.code
    class Meta:
        verbose_name = '3-File Type'

class Batch(models.Model):
    class BatchStatus(models.TextChoices):
        PENDING = 'pending', _('Pending')
        PROCESSING = 'processing', _('Processing')
        DONE = 'Done', _('Done')
    bank_id = models.ForeignKey(Bank,related_name='batch_bank',on_delete=models.CASCADE,unique=False,blank=False,null=False)
    file_type_id = models.ForeignKey(FileTypes,related_name='file_types_bank',on_delete=models.CASCADE,unique=False,blank=False,null=True)
    status = models.CharField(max_length=30, choices= BatchStatus.choices,default=BatchStatus.PENDING)
    number_files_submitted = models.IntegerField(blank=True, null=True)
    store_path = models.CharField(max_length=200, blank=True)
    processed_time = models.DateTimeField(default=datetime.now, blank=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.bank_id.name+ '--' +self.status + "--" + str(self.bank_id.id)
    class Meta:
        verbose_name = '2-Batch'


def get_file_path(instance, filename):
    print(instance, filename)
    ext = filename.split('.')[-1]
    codedFilename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(instance.batch_id.bank_id.name + '/' +instance.batch_id.file_type_id.code, codedFilename)

class File(models.Model):
    batch_id = models.ForeignKey(Batch,related_name='file_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
    file_url = models.FileField('File Path', upload_to = get_file_path, blank=True,null=True)
    file_name  = models.CharField(max_length=100, blank=True, unique=False, )
    file_format = models.CharField(max_length=100, blank=True, unique=False, )
    lastModified = models.IntegerField(blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    
    create_on = models.DateTimeField(default=datetime.now, blank=True, )
    def __str__(self):
        return self.file_name
    class Meta:
        verbose_name = '4-File'

