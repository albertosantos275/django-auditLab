from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from a_account import views
from rest_framework.routers import DefaultRouter

app_name= 'a_account'



urlpatterns = [

    # User API
    path('user/', views.UserAPIView.as_view()),
    path('user/<int:id>/',views.UserAPIView.as_view()),  
    path('api/token/', views.LoginAPIView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


]