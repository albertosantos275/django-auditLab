from django.shortcuts import render
import json
from rest_framework.permissions import IsAuthenticated,AllowAny
# Create your views here.
from rest_framework import generics, status
from rest_framework import mixins
from django.shortcuts import render, redirect,HttpResponse
import django_filters
from a_account.serializers import UserSerializer,LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from django.contrib.auth import get_user_model
user = get_user_model()


class UserAPIView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin,
                            mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):

    serializer_class = UserSerializer
    queryset = user.objects.all()
    #for url pattern
    lookup_field = 'id'

    #with this authetification we use username and password basic auth
    #authentication_classes = [SessionAuthentication,BasicAuthentication]

    #TODO with this authetification we use token authentification ()
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
        print(request.data)

        return self.update(request,id)

    def delete(self,request,id):

        return  self.destroy(request,id)

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        
        isValid = serializer.is_valid()
        print('is valid -- ', isValid)
        if not isValid:
            data={}
            data['error']= serializer.errors
            return HttpResponse(json.dumps(data),content_type="application/json") 
        else:      
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
    # def  get_queryset(self): 
    #     user_id = self.request.user
    #     user = get_user_model()
    #     return user.objects.filter(id=user_id.id)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = authenticate(username=username, password=password)
        token = LoginSerializer.get_token(user).access_token
       
        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't  have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        # serializer = self.serializer_class(data=user)
        # serializer.is_valid(raise_exception=True)
        data_dict={}
        data_dict['access'] = str(token)
        data_dict['username'] = username
        data_dict['is_admin'] = user.is_admin
        data_dict['userId'] = user.id
        data_dict['refresh'] = ''
        data_json =  json.loads(json.dumps(data_dict))

        return Response(data_json, status=status.HTTP_200_OK)
