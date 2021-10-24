from django.db import models
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
import uuid
import os
from pathlib import Path
from django.db.models import signals
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.



#Reference 
class Activity(models.Model):    
    code_ciiv = models.CharField(max_length=100, blank=False, unique=True)
    macro = models.CharField(max_length=80, blank=True, unique=False)
    activity = models.CharField(max_length=100, blank=True, unique=False)
    precedent_crime_ids =  models.ManyToManyField('PrecendentCrime',blank=True, unique=False)
    risk_ids =  models.ManyToManyField('Risk',blank=True, unique=False)

    create_on = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.macro + ' -- ' +  self.activity
    class Meta:
        verbose_name = 'R1- Activity Types'

class Risk(models.Model):    
    name = models.CharField(max_length=100, blank=False, unique=True)
    code = models.CharField(max_length=20, blank=False, unique=True)

    create_on = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'R2- Risk Types'

class PrecendentCrime(models.Model):    
    name = models.CharField(max_length=100, blank=False, unique=True)
    code = models.CharField(max_length=20, blank=False, unique=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name 
    class Meta:
        verbose_name = 'R3- Crime Types'




#This model are goinggto be move to a separate app

#By Activity
class ReportByActivity(models.Model): 
    batch_id = models.ForeignKey('a_bank.Batch',related_name='report_activity_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)   
    activity_id = models.ForeignKey(Activity,related_name='activity_type_batch',on_delete=models.CASCADE,unique=False,blank=True,null=True)
    precendent_crime_id = models.ForeignKey(PrecendentCrime,related_name='precedent_crime_risk_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=True)
    risk_id = models.ForeignKey(Risk,related_name='risk_batch',on_delete=models.CASCADE,unique=False,blank=False,null=True)
    total = models.IntegerField(blank=True, null=True)
    create_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.batch_id.bank_id.name

    class Meta:
        verbose_name = '8.0- Report By Activity'


#By Operation
class OperationType(models.Model):    
    name = models.CharField(max_length=100, blank=False, unique=True)
    code = models.CharField(max_length=20, blank=True, unique=False)
    create_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'R4- Operation Type'

class ReportByOperation(models.Model):
    batch_id = models.ForeignKey('a_bank.Batch',related_name='report_operation_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)    
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
        verbose_name = 'R5- Person Type'

class ReportByPerson(models.Model):
    batch_id = models.ForeignKey('a_bank.Batch',related_name='report_person_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)       
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
        verbose_name = 'R6- Service Type'

class ReportByService(models.Model):
    batch_id = models.ForeignKey('a_bank.Batch',related_name='report_sercvice_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)   
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
    batch_id = models.ForeignKey('a_bank.Batch',related_name='report_suspicous_activity_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)   
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