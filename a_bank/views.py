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
from a_bank.models import Bank
from a_bank.serializers import BankSerializer


class NewspaperBank(django_filters.FilterSet):

    class Meta:
        model = Bank
        fields = ['name']

#Bank Api View
class  BankAPIView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin,
                            mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):

    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    filter_class = NewspaperBank
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

