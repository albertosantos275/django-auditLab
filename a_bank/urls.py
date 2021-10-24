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

        # file API
    path('file_types/<int:id>/',views.FileTypesAPIView.as_view()),
    path('file_types/', views.FileTypesAPIView.as_view()),

    # batch API
    path('batchs/<int:id>/',views.BatchAPIView.as_view()),
    path('batchs/', views.BatchAPIView.as_view()),


    #test function view
   path('test_app/',views.test_views, name='test_views'),



]