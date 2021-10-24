from django.shortcuts import render
from django.http import HttpResponse
from dateutil.parser import parse
import json

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins
from django.shortcuts import render
import django_filters
from a_bank.models import Bank, Batch, File, Risk,FileTypes
from a_bank.serializers import BankSerializer, FileSerializer, BatchSerializer,FileTypesSerializer
from datetime import timedelta
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

class BankFilter(django_filters.FilterSet):

    class Meta:
        model = Bank
        fields = ['name']

#Bank Api View
class  BankAPIView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin,
                            mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):

    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    filter_class = BankFilter
    #for url pattern
    lookup_field = 'id'

    permission_classes = [IsAuthenticated]

    def get(self,request,id = None):
        if id:
            return self.retrieve(request)
        else:
            #if id = 0 show all the records
            return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self,request,id=None):

        return self.update(request,id)

    def delete(self,request,id):

        return  self.destroy(request,id)

class FileFilter(django_filters.FilterSet):

    class Meta:
        model = File
        fields = ['file_name']

#File Api View
class  FileAPIView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin,
                            mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):

    serializer_class = FileSerializer
    queryset = File.objects.all()
    filter_class = FileFilter
    #for url pattern
    lookup_field = 'id'

    permission_classes = [IsAuthenticated]

    def get(self,request,id = None):
        if id:
            return self.retrieve(request)
        else:
            #if id = 0 show all the records
            return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self,request,id=None):

        return self.update(request,id)

    def delete(self,request,id):

        return  self.destroy(request,id)

class BatchFilter(django_filters.FilterSet):

    class Meta:
        model = Batch
        fields = ['file_type_id','bank_id']

#Batch Api View
class  BatchAPIView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin,
                            mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):

    serializer_class = BatchSerializer
    queryset = Batch.objects.all()
    filter_class = BatchFilter
    #for url pattern
    lookup_field = 'id'

    permission_classes = [IsAuthenticated]

    def get(self,request,id = None):
        if id:
            return self.retrieve(request)
        else:
            #if id = 0 show all the records
            return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self,request,id=None):

        return self.update(request,id)

    def delete(self,request,id):

        return  self.destroy(request,id)



class FileTypesFilter(django_filters.FilterSet):

    class Meta:
        model = FileTypes
        fields = ['code','name']

#FileTypes Api View
class  FileTypesAPIView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin,
                            mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):

    serializer_class = FileTypesSerializer
    queryset = FileTypes.objects.all()
    filter_class = FileTypesFilter
    #for url pattern
    lookup_field = 'id'

    permission_classes = [IsAuthenticated]

    def get(self,request,id = None):
        if id:
            return self.retrieve(request)
        else:
            #if id = 0 show all the records
            return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self,request,id=None):

        return self.update(request,id)

    def delete(self,request,id):

        return  self.destroy(request,id)




from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from a_bank.models import Activity, PrecendentCrime,Risk,ReportByActivity,OperationType,ReportByOperation,ReportByPerson,PersonType,ServiceType,ReportByService,ReportBySuspicious
from datetime import datetime

@csrf_exempt
@require_http_methods(["GET","POST"])
def report_data_endpoint(request): 

    if request.method=='POST':
        body_unicode = request.body
        body = json.loads(body_unicode)


            # "610b420405935ed1c8766b6a" : {
            #   "average" : 2078045.0,
            #   "avg_o_act_avg" : false,
            #   "lastname" : "Hayes",
            #   "name" : "Kathy",
            #   "total" : 2078045,
            #   "total_o_act_avg" : false,
            #   "transactions" : 1
            # }



            # class ReportBySuspicious(models.Model):
            #     batch_id = models.ForeignKey(Batch,related_name='report_suspicous_activity_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)   
            #     activity_id = models.ForeignKey(Activity,related_name='suspicous_activity_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
            #     transaction_id = models.CharField(max_length=100, blank=True, unique=False)
            #     lastname = models.CharField(max_length=100, blank=True, unique=False)
            #     name = models.CharField(max_length=100, blank=True, unique=False)
            #     avg_o_act_avg = models.BooleanField(default=False)
            #     total_o_act_avg = models.BooleanField(default=False)
            #     transactions = models.IntegerField(blank=True, null=True)
            #     total = models.IntegerField(blank=True, null=True)
            #     create_on = models.DateTimeField(default=datetime.now, blank=True)




        # #By BySuspicious 
        # data_by_activity = body['result']['by_suspicious']['agregates']
        # json_res = {}

        # for item in data_by_activity.keys():
            
        #     opera = Activity.objects.filter( code_ciiv = item)
        #     batch = Batch.objects.all()[0]
        #     if len(opera) > 0:
        #         lista =  data_by_activity[item].keys()
        #         print(data_by_activity[item]['agregates'].keys())
        #         for kdarta in data_by_activity[item]['agregates'].keys():                    
        #             report = ReportBySuspicious(batch_id=batch, activity_id=opera[0], 
        #                                     total=data_by_activity[item]['agregates'][kdarta]['total'], 
        #                                     lastname=data_by_activity[item]['agregates'][kdarta]['lastname'],
        #                                     name=data_by_activity[item]['agregates'][kdarta]['name'],
        #                                     avg_o_act_avg=data_by_activity[item]['agregates'][kdarta]['avg_o_act_avg'],
        #                                     total_o_act_avg=data_by_activity[item]['agregates'][kdarta]['avg_o_act_avg'],
        #                                     transaction_id=kdarta,
        #                                     transactions=data_by_activity[item]['agregates'][kdarta]['transactions']
                                            
        #                                     )
        #             report.save()
        #     else:
        #         print(item)
  








        # #By Service 
        # data_by_activity = body['result']['by_service']['agregates']
        # json_res = {}
        # print(data_by_activity.keys())

        # for item in data_by_activity.keys():
            
        #     opera = ServiceType.objects.filter( name = data_by_activity[item]['service'])
        #     batch = Batch.objects.all()[0]
        #     if len(opera) > 0:
        #         report = ReportByService(batch_id=batch,service_type_id=opera[0], total=data_by_activity[item]['total'], phase=data_by_activity[item]['phase'].encode(encoding="ascii",errors="xmlcharrefreplace") )
        #         report.save()
        #     else:
        #         operNew =  ServiceType(code = str(item), name = data_by_activity[item]['service'])
        #         print(data_by_activity[item]['service'])
        #         operNew.save()
        #         report = ReportByService(batch_id=batch,service_type_id=operNew, total=data_by_activity[item]['total'], phase=data_by_activity[item]['phase'] )
        #         report.save()


        # #By Person 
        # data_by_activity = body['result']['by_person']['agregates']
        # json_res = {}
        # print(data_by_activity.keys())

        # for item in data_by_activity.keys():
            
        #     opera = PersonType.objects.filter(code = item)
        #     batch = Batch.objects.all()[0]
        #     if len(opera) > 0:
        #         report = ReportByPerson(batch_id=batch,person_type_id=opera[0], total=data_by_activity[item]['total'], risk=data_by_activity[item]['risk'] )
        #         report.save()
        #     else:
        #         operNew =  PersonType(name = data_by_activity[item]['user'],code=item)
        #         operNew.save()
        #         report = ReportByPerson(batch_id=batch,person_type_id=operNew, total=data_by_activity[item]['total'], risk=data_by_activity[item]['risk'] )
        #         report.save()





        # #By operation 
        # data_by_activity = body['result']['by_operations']['agregates']
        # json_res = {}
        # print(data_by_activity.keys())

        # for item in data_by_activity.keys():
            
        #     opera = OperationType.objects.filter(name = data_by_activity[item]['operation'])
        #     batch = Batch.objects.all()[0]
        #     if len(opera) > 0:
        #         report = ReportByOperation(batch_id=batch,operation_id=opera[0], total=data_by_activity[item]['total'] )
        #         report.save()
        #     else:
        #         operNew =  OperationType(name = data_by_activity[item]['operation'],code='OP')
        #         operNew.save()
        #         report = ReportByOperation(batch_id=batch,operation_id=operNew, total=data_by_activity[item]['total'] )
        #         report.save()








        # data_by_activity = body['result']['by_activity']['agregates']
        # for item in data_by_activity.keys():
        #     data = data_by_activity[item]['agregates']
            # if item[0]=='D':
            #     for key in data.keys():
            #         # batch_id = models.ForeignKey(Batch,related_name='report_activity_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)   
            #         # precendent_crime_id = models.ForeignKey(PrecendentCrime,related_name='precedent_crime_risk_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
            #         # risk_id = models.ForeignKey(Risk,related_name='risk_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
            #         # total = models.IntegerField(blank=True, null=True)
            #         batch = Batch.objects.all()[0]
            #         print('ggggggggggggggggggggggggg  ',key.strip())
            #         precedent  = PrecendentCrime.objects.filter(name__contains = key)
            #         if len(precedent) > 0:  
            #             print('data[key] ',data[key])              
            #             activityReport = ReportByActivity(batch_id=batch,precendent_crime_id=precedent[0], total=data[key]['total'] )
            #             activityReport.save()
            # if item[0]=='R':
            #     for key in data.keys():
            #         # batch_id = models.ForeignKey(Batch,related_name='report_activity_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)   
            #         # precendent_crime_id = models.ForeignKey(PrecendentCrime,related_name='precedent_crime_risk_type_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
            #         # risk_id = models.ForeignKey(Risk,related_name='risk_batch',on_delete=models.CASCADE,unique=False,blank=False,null=False)
            #         # total = models.IntegerField(blank=True, null=True)
            #         batch = Batch.objects.all()[0]
            #         print('ggggggggggggggggggggggggg  ',key.strip())
            #         risk  = Risk.objects.filter(name__contains = key)
            #         if len(risk) > 0:  
            #             print('data[key] ',data[key])              
            #             activityReport = ReportByActivity(batch_id=batch,risk_id=risk[0], total=data[key]['total'] )
            #             activityReport.save()

        json_res={}

        return HttpResponse(json_res, content_type='application/json')
    
    

###########################################################################################




from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from a_bank.models import Activity, PrecendentCrime,Risk
from datetime import datetime
from a_bank.tasks import launch_create_report


@csrf_exempt
@require_http_methods(["GET", "POST"])
def test_views(request):

    if request.method == 'POST':
        json_res = {}
        bank_id = request.POST.get('bank_id', '')
        file_type_id = request.POST.get('file_type_id', '')

        number_files = len(request.FILES.getlist('files'))
        print('POST DATa  === >', bank_id, file_type_id)

        bank = Bank.objects.get(id=bank_id)
        file_type = FileTypes.objects.get(id=file_type_id)
        batch = Batch(bank_id=bank, file_type_id=file_type,
                      number_files_submitted=number_files)
        batch.save()
        for f in request.FILES.getlist('files'):
            file = File(file_url=f, batch_id=batch, file_name=f.name,
                        file_format=f.content_type, file_size=f.size
                        )
            file.save()


        BASE_DIR = Path(__file__).resolve().parent.parent
        MEDIA_DIR = os.path.join(BASE_DIR, 'media')

        # # if not instance.is_verified:
        #     # Send verification email
        print('Calling Asyync task after bastch created ')
        file_paths = File.objects.filter(batch_id=batch.id).values_list('file_url', flat=True)
        
        absolute_files_path = []
        if len(file_paths) > 0:
            for path in file_paths:
                absolute_files_path.append(MEDIA_DIR + '/' + path)

        # # TODO method to report
        batch_info = {}
        batch_info['batch_id'] = batch.id
        # MEDIA_DIR + '/' +  batch.bank_id.name + '/' + batch.file_type_id.code + '/'
        print('Files number path :  ', absolute_files_path)
        batch_info['absolute_files_path'] = absolute_files_path
        batch_info['file_type_id'] = batch.file_type_id.id
        batch_info['file_type_code'] = batch.file_type_id.code
        batch_info['result_storage_path'] = MEDIA_DIR + '/' + 'ResultStorage'
        print('batch_info ', batch_info)

        launch_create_report.delay(batch_info)
 
        # print(created_file)



        return HttpResponse(json_res, content_type='application/json')













    # if request.method=='GET':


    #     # activities =  Activity.objects.filter(macro='Agricultura_test')
    #     # activities.delete()

    #     ## test to copy m,any input at once
    #     # now = datetime.now()
    #     # current_time = now.strftime("%H:%M:%S")
    #     # print(" Time Start =", current_time)

    #     # thing_objects = []
        
    #     # for i in range(0,1000000):
    #     #     new_activity = Activity(code_ciiv='9999999'+str(i), macro='Agricultura_test',
    #     #                             activity='10000 Agricultura',
    #     #                             DP1='Actividad Comercial sin Permisos Correspondientes',
    #     #                             DP2='Actividad Comercial sin Permisos Correspondientes',
    #     #                             DP3='Actividad Comercial sin Permisos Correspondientes',
    #     #                             R1='test data',
    #     #                             R2='test data',
    #     #                             R3='test data'
    #     #                             )
    #     #     thing_objects.append(new_activity)

    #     # Activity.objects.bulk_create(thing_objects)    

    #     # now = datetime.now()

    #     # current_time = now.strftime("%H:%M:%S")
    #     # print(" Time End =", current_time)

    #     #     new_activity.precedent_crime_ids.add(1, 2, 4)
    #     #     new_activity.risk_ids.add(1, 2, 4)



    #     # for crime in PrecendentCrime.objects.all():
    #     #     activities =  Activity.objects.filter(DP3=crime.name)
    #     #     if len(activities) > 0:
    #     #         for acti in activities:
    #     #             acti.precedent_crime_ids.add(crime.id)
    #     #             print(acti.DP3, crime.name)

    #     # for risk in Risk.objects.all():
    #     #     activities =  Activity.objects.filter(R3=risk.name)
    #     #     if len(activities) > 0:
    #     #         for acti in activities:
    #     #             acti.risk_ids.add(risk.id)
    #     #             print(acti.R3, risk.name)
                    
    #                 # print('==', acti.activity,len(acti.risk_ids.all()))
    #                 # for test in acti.risk_ids.all():
    #                 #     print(test.name)

    #     # print('getting data processs ======================> ',list(Activity.objects.distinct().values_list('DP1',flat=True)))
    #     # risks = list(Activity.objects.distinct().values_list('R3',flat=True))
    #     # for i in range(0, len(risks)):
    #     #     risk_query = Risk.objects.filter(  
                            
    #     #         name = risks[i]
    #     #     )
    #     #     if len(risk_query) == 0:
    #     #         risk =  Risk(

    #     #             name = risks[i],
    #     #             code = 'R' + str(i)
    #     #         )
    #     #         risk.save()







    #     # print('getting data processs ======================> ',list(Activity.objects.distinct().values_list('DP1',flat=True)))
    #     # crimes = list(Activity.objects.distinct().values_list('DP3',flat=True))
    #     # for i in range(0, len(crimes)):
    #     #     crime_query = PrecendentCrime.objects.filter(  
                            
    #     #         name = crimes[i]
    #     #     )
    #     #     if len(crime_query) == 0:
    #     #         precent_crime =  PrecendentCrime(

    #     #             name = crimes[i],
    #     #             code = 'DPnew' + str(i)
    #     #         )
    #     #         precent_crime.save()


    #     json_res = {}
    #     return HttpResponse(json_res,content_type='application/json')

