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
from a_bank.models import Activity, PrecendentCrime,Risk
from datetime import datetime

@csrf_exempt
@require_http_methods(["GET","POST"])
def test_views(request):  

    if request.method=='POST':
        print(request.POST)
        json_res = {}
        bank_id = request.POST.get('bank_id', '')
        file_type_id = request.POST.get('file_type_id', '')

        number_files = len(request.FILES.getlist('files'))
        bank = Bank.objects.get(id=bank_id)
        file_type = FileTypes.objects.get(id=file_type_id)
        batch = Batch(bank_id=bank, file_type_id=file_type, number_files_submitted = number_files)
        batch.save()
        for f in request.FILES.getlist('files'):
            file = File(file_url=f, batch_id=batch, file_name=f.name,
                       file_format=f.content_type, file_size=f.size
                       
                       )
            file.save()

        return HttpResponse(json_res, content_type='application/json')

    
    if request.method=='GET':


        # activities =  Activity.objects.filter(macro='Agricultura_test')
        # activities.delete()

        ## test to copy m,any input at once
        # now = datetime.now()
        # current_time = now.strftime("%H:%M:%S")
        # print(" Time Start =", current_time)

        # thing_objects = []
        
        # for i in range(0,1000000):
        #     new_activity = Activity(code_ciiv='9999999'+str(i), macro='Agricultura_test',
        #                             activity='10000 Agricultura',
        #                             DP1='Actividad Comercial sin Permisos Correspondientes',
        #                             DP2='Actividad Comercial sin Permisos Correspondientes',
        #                             DP3='Actividad Comercial sin Permisos Correspondientes',
        #                             R1='test data',
        #                             R2='test data',
        #                             R3='test data'
        #                             )
        #     thing_objects.append(new_activity)

        # Activity.objects.bulk_create(thing_objects)    

        # now = datetime.now()

        # current_time = now.strftime("%H:%M:%S")
        # print(" Time End =", current_time)

        #     new_activity.precedent_crime_ids.add(1, 2, 4)
        #     new_activity.risk_ids.add(1, 2, 4)



        # for crime in PrecendentCrime.objects.all():
        #     activities =  Activity.objects.filter(DP3=crime.name)
        #     if len(activities) > 0:
        #         for acti in activities:
        #             acti.precedent_crime_ids.add(crime.id)
        #             print(acti.DP3, crime.name)

        # for risk in Risk.objects.all():
        #     activities =  Activity.objects.filter(R3=risk.name)
        #     if len(activities) > 0:
        #         for acti in activities:
        #             acti.risk_ids.add(risk.id)
        #             print(acti.R3, risk.name)
                    
                    # print('==', acti.activity,len(acti.risk_ids.all()))
                    # for test in acti.risk_ids.all():
                    #     print(test.name)

        # print('getting data processs ======================> ',list(Activity.objects.distinct().values_list('DP1',flat=True)))
        # risks = list(Activity.objects.distinct().values_list('R3',flat=True))
        # for i in range(0, len(risks)):
        #     risk_query = Risk.objects.filter(  
                            
        #         name = risks[i]
        #     )
        #     if len(risk_query) == 0:
        #         risk =  Risk(

        #             name = risks[i],
        #             code = 'R' + str(i)
        #         )
        #         risk.save()







        # print('getting data processs ======================> ',list(Activity.objects.distinct().values_list('DP1',flat=True)))
        # crimes = list(Activity.objects.distinct().values_list('DP3',flat=True))
        # for i in range(0, len(crimes)):
        #     crime_query = PrecendentCrime.objects.filter(  
                            
        #         name = crimes[i]
        #     )
        #     if len(crime_query) == 0:
        #         precent_crime =  PrecendentCrime(

        #             name = crimes[i],
        #             code = 'DPnew' + str(i)
        #         )
        #         precent_crime.save()


        json_res = {}
        return HttpResponse(json_res,content_type='application/json')

