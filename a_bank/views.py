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
from a_bank.models import Bank, Batch, File, Risk
from a_bank.serializers import BankSerializer, FileSerializer, BatchSerializer


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
        fields = ['status']

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



from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from a_bank.models import Activity, PrecendentCrime,Risk

@csrf_exempt
@require_http_methods(["GET","POST"])
def test_views(request):  
    
    if request.method=='GET':

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

