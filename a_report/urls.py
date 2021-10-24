

from django.urls import path
from a_report import views

app_name= 'a_report'

urlpatterns = [

    #report end point
   path('report_end_point/',views.report_data_endpoint, name='report_end_point'),

]
