from django.urls import path
from a_bank import views

app_name= 'a_bank'

urlpatterns = [

    # bank API
    path('bank/<int:id>/',views.BankAPIView.as_view()),
    path('bank/', views.BankAPIView.as_view()),

    # file API
    path('file/<int:id>/',views.FileAPIView.as_view()),
    path('file/', views.FileAPIView.as_view()),

    # batch API
    path('batch/<int:id>/',views.BatchAPIView.as_view()),
    path('batch/', views.BatchAPIView.as_view()),


]