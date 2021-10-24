


from dateutil.parser import parse
import json

# Create your views here.
from a_report.models import Risk
from a_bank.models import Bank, Batch, File,FileTypes
from a_bank.serializers import BankSerializer, FileSerializer, BatchSerializer,FileTypesSerializer
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from a_report.models import Activity, PrecendentCrime,Risk,ReportByActivity,OperationType,ReportByOperation,ReportByPerson,PersonType,ServiceType,ReportByService,ReportBySuspicious
from datetime import datetime
from datetime import timedelta
from pathlib import Path
import os
# Create your views here.



###########################################################################################
# Use these to creeate the parser for the json file file that goes into the db


# @csrf_exempt
# @require_http_methods(["GET","POST"])
def report_insert_db(): 
    print('aqui')

    load_data =  open('../media/ResultStorage/1635057811.json', 'r')
    data_file =  json.loads(load_data.read())
    load_data.close()
    body=  data_file

    print("Start Report Insertiing in DB ... ")



    #By Activity 
    data_by_activity = body['by_activity']['agregates']
    for item in data_by_activity.keys():
        data = data_by_activity[item]['agregates']

        
        if item[0]=='D':
            for key in data.keys():
                # batch_id = models.ForeignKey(Batch,related_name='report_activity_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)   
                # precendent_crime_id = models.ForeignKey(PrecendentCrime,related_name='precedent_crime_risk_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
                # risk_id = models.ForeignKey(Risk,related_name='risk_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
                # total = models.IntegerField(blank=True, null=True)
                batch = Batch.objects.all()[0]
                print('ggggggggggggggggggggggggg  ',key.strip())
                precedent  = PrecendentCrime.objects.filter(name__contains = key)
                if len(precedent) > 0:  
                    print('data[key] ',data[key])              
                    activityReport = ReportByActivity(batch_id=batch,precendent_crime_id=precedent[0], total=data[key]['total'] )
                    activityReport.save()
        if item[0]=='R':
            for key in data.keys():
                # batch_id = models.ForeignKey(Batch,related_name='report_activity_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)   
                # precendent_crime_id = models.ForeignKey(PrecendentCrime,related_name='precedent_crime_risk_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
                # risk_id = models.ForeignKey(Risk,related_name='risk_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
                # total = models.IntegerField(blank=True, null=True)
                batch = Batch.objects.all()[0]
                print('ggggggggggggggggggggggggg  ',key.strip())
                risk  = Risk.objects.filter(name__contains = key)
                if len(risk) > 0:  
                    print('data[key] ',data[key])              
                    activityReport = ReportByActivity(batch_id=batch,risk_id=risk[0], total=data[key]['total'] )
                    activityReport.save()















    #By BySuspicious 
    data_by_activity = body['by_suspicious']['agregates']
    json_res = {}

    for item in data_by_activity.keys():
        
        opera = Activity.objects.filter( code_ciiv = int(item))

        batch = Batch.objects.all()[0]
        if len(opera) > 0:
            lista =  data_by_activity[item].keys()
            print(data_by_activity[item]['agregates'].keys())
            for kdarta in data_by_activity[item]['agregates'].keys():  
                print(opera[0].id)                 
                report = ReportBySuspicious(batch_id=batch, activity_id=opera[0], 
                                        total=data_by_activity[item]['agregates'][kdarta]['total'], 
                                        lastname=data_by_activity[item]['agregates'][kdarta]['lastname'],
                                        name=data_by_activity[item]['agregates'][kdarta]['name'],
                                        avg_o_act_avg=data_by_activity[item]['agregates'][kdarta]['avg_o_act_avg'],
                                        total_o_act_avg=data_by_activity[item]['agregates'][kdarta]['avg_o_act_avg'],
                                        transaction_id=kdarta,
                                        transactions=data_by_activity[item]['agregates'][kdarta]['transactions']
                                        
                                        )
                report.save()
        else:
            print(item)


    #By Service 
    data_by_activity = body['by_service']['agregates']
    json_res = {}
    print(data_by_activity.keys())

    for item in data_by_activity.keys():
        
        opera = ServiceType.objects.filter( name = data_by_activity[item]['service'])
        batch = Batch.objects.all()[0]
        if len(opera) > 0:
            report = ReportByService(batch_id=batch,service_type_id=opera[0], total=data_by_activity[item]['total'], phase=data_by_activity[item]['phase'].encode(encoding="ascii",errors="xmlcharrefreplace") )
            report.save()
        else:
            operNew =  ServiceType(code = str(item), name = data_by_activity[item]['service'])
            print(data_by_activity[item]['service'])
            operNew.save()
            report = ReportByService(batch_id=batch,service_type_id=operNew, total=data_by_activity[item]['total'], phase=data_by_activity[item]['phase'] )
            report.save()


    #By Person 
    data_by_activity = body['by_person']['agregates']
    json_res = {}
    print(data_by_activity.keys())

    for item in data_by_activity.keys():
        
        opera = PersonType.objects.filter(code = item)
        batch = Batch.objects.all()[0]
        if len(opera) > 0:
            report = ReportByPerson(batch_id=batch,person_type_id=opera[0], total=data_by_activity[item]['total'], risk=data_by_activity[item]['risk'] )
            report.save()
        else:
            operNew =  PersonType(name = data_by_activity[item]['user'],code=item)
            operNew.save()
            report = ReportByPerson(batch_id=batch,person_type_id=operNew, total=data_by_activity[item]['total'], risk=data_by_activity[item]['risk'] )
            report.save()


    #By operation 
    data_by_activity = body['by_operations']['agregates']
    json_res = {}
    print(data_by_activity.keys())

    for item in data_by_activity.keys():
        
        opera = OperationType.objects.filter(name = data_by_activity[item]['operation'])
        batch = Batch.objects.all()[0]
        if len(opera) > 0:
            report = ReportByOperation(batch_id=batch,operation_id=opera[0], total=data_by_activity[item]['total'] )
            report.save()
        else:
            operNew =  OperationType(name = data_by_activity[item]['operation'],code='OP')
            operNew.save()
            report = ReportByOperation(batch_id=batch,operation_id=operNew, total=data_by_activity[item]['total'] )
            report.save()



 


        print("Report Inserted in DB ... ")


##########################################################################################




















