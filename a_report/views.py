from django.shortcuts import render
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
from a_report.models import Risk
from a_bank.models import Bank, Batch, File,FileTypes
from a_bank.serializers import BankSerializer, FileSerializer, BatchSerializer,FileTypesSerializer
from datetime import timedelta
from pathlib import Path
from a_report.report_insert import report_insert_db
import os
# Create your views here.



###########################################################################################
# Use these to creeate the parser for the json file file that goes into the db
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from a_report.models import Activity, PrecendentCrime,Risk,ReportByActivity,OperationType,ReportByOperation,ReportByPerson,PersonType,ServiceType,ReportByService,ReportBySuspicious
from datetime import datetime

@csrf_exempt
@require_http_methods(["GET","POST"])
def report_data_endpoint(request): 
    report_insert_db()
    print('aqui')
    json_res = {}
    return HttpResponse(json_res,content_type='application/json')