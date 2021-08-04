from django.urls import path
from a_bank import views

app_name= 'a_bank'

urlpatterns = [

    # Article API
    path('bank/<int:id>/',views.BankAPIView.as_view()),
    path('bank/', views.BankAPIView.as_view()),



]