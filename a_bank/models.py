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

# def batch_post_save(sender, instance, signal, *args, **kwargs):
 
# signals.post_save.connect(batch_post_save, sender=Batch)





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


class Activity(models.Model):    
    code_ciiv = models.CharField(max_length=100, blank=False, unique=True)
    macro = models.CharField(max_length=80, blank=True, unique=False)
    activity = models.CharField(max_length=100, blank=True, unique=False)
    precedent_crime_ids =  models.ManyToManyField('PrecendentCrime',blank=True, unique=False)
    risk_ids =  models.ManyToManyField('Risk',blank=True, unique=False)

    DP1 = models.CharField(max_length=250, blank=True, unique=False)
    DP2 = models.CharField(max_length=250, blank=True, unique=False)
    DP3 = models.CharField(max_length=250, blank=True, unique=False)

    R1 = models.CharField(max_length=250, blank=True, unique=False)
    R2 = models.CharField(max_length=250, blank=True, unique=False)
    R3 = models.CharField(max_length=250, blank=True, unique=False)

    create_on = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.macro + ' -- ' +  self.activity
    class Meta:
        verbose_name = '5- Activity'

class Risk(models.Model):    
    name = models.CharField(max_length=100, blank=False, unique=True)
    code = models.CharField(max_length=20, blank=False, unique=True)

    create_on = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = '6- Risk'

class PrecendentCrime(models.Model):    
    name = models.CharField(max_length=100, blank=False, unique=True)
    code = models.CharField(max_length=20, blank=False, unique=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name 
    class Meta:
        verbose_name = '7- Crime'




#This model are goin gto be move to a separate app

#By Activity
class ReportByActivity(models.Model): 
    batch_id = models.ForeignKey(Batch,related_name='report_activity_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)   
    precendent_crime_id = models.ForeignKey(PrecendentCrime,related_name='precedent_crime_risk_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=True)
    risk_id = models.ForeignKey(Risk,related_name='risk_batch',on_delete=models.CASCADE,unique=False,blank=False,null=True)
    total = models.IntegerField(blank=True, null=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.batch_id.bank_id.name

    class Meta:
        verbose_name = '8.0- Report Precedent Crime and Risk'


#By Operation
class OperationType(models.Model):    
    name = models.CharField(max_length=100, blank=False, unique=True)
    code = models.CharField(max_length=20, blank=True, unique=False)
    create_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = '9.2- Operation Type'

class ReportByOperation(models.Model):
    batch_id = models.ForeignKey(Batch,related_name='report_operation_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)    
    operation_id = models.ForeignKey(OperationType,related_name='operatioon_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
    total = models.IntegerField(blank=True, null=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.operation_id.name

    class Meta:
        verbose_name = '8.1- Report By Operations'





#By Person
class PersonType(models.Model):    
    name = models.CharField(max_length=100, blank=False, unique=True)
    code = models.CharField(max_length=20, blank=False, unique=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = '9.3- Person Type'

class ReportByPerson(models.Model):
    batch_id = models.ForeignKey(Batch,related_name='report_person_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)       
    person_type_id = models.ForeignKey(PersonType,related_name='person_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
    risk = models.CharField(max_length=100, blank=False, unique=False)
    total = models.IntegerField(blank=True, null=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.person_type_id.name

    class Meta:
        verbose_name = '8.2- Report by Person Type'



#By Service
class ServiceType(models.Model):    
    name = models.CharField(max_length=100, blank=False, unique=True)
    code = models.CharField(max_length=20, blank=True, unique=False)
    create_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = '9.1- Service Type'

class ReportByService(models.Model):
    batch_id = models.ForeignKey(Batch,related_name='report_sercvice_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)   
    service_type_id = models.ForeignKey(ServiceType,related_name='service_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
    phase = models.CharField(max_length=100, blank=True, unique=False)
    total = models.IntegerField(blank=True, null=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.service_type_id.name 

    class Meta:
        verbose_name = '8.3- Report By Service'


            # "610b420405935ed1c8766b6a" : {
            #   "average" : 2078045.0,
            #   "avg_o_act_avg" : false,
            #   "lastname" : "Hayes",
            #   "name" : "Kathy",
            #   "total" : 2078045,
            #   "total_o_act_avg" : false,
            #   "transactions" : 1
            # }



class ReportBySuspicious(models.Model):
    batch_id = models.ForeignKey(Batch,related_name='report_suspicous_activity_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)   
    activity_id = models.ForeignKey(Activity,related_name='suspicous_activity_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
    transaction_id = models.CharField(max_length=100, blank=True, unique=False)
    lastname = models.CharField(max_length=100, blank=True, unique=False)
    name = models.CharField(max_length=100, blank=True, unique=False)
    avg_o_act_avg = models.BooleanField(default=False)
    total_o_act_avg = models.BooleanField(default=False)
    transactions = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.transaction_id + '-' + self.lastname

    class Meta:
        verbose_name = '8.4- Report By Suspicous'