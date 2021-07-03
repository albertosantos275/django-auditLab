from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email','last_login',"is_superuser","is_admin","is_active","company_name","company_address","company_telephone","password")
        extra_kwargs = {
            'password': {'write_only': True,'required': False},
        }
        read_only_fields = ('id',)
        write_only_fields = ('password',)


    def create(self, validated_data):
        # print(validated_data)
        # locations = validated_data.pop('locations')
        # print("ffff",locations)
        print('aquirrrr')
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            company_name=validated_data['company_name'],
            company_address=validated_data['company_address'],
            company_telephone=validated_data['company_telephone'],
            is_superuser=validated_data['is_superuser'],
            is_admin=validated_data['is_admin'],
            is_active=validated_data['is_active'],           
           
         
        )   

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        print('Updating --- > ')        
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.company_address = validated_data.get('company_address', instance.company_address)
        instance.company_telephone = validated_data.get('company_telephone', instance.company_telephone)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        print(validated_data)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])


        instance.save()
   
        return instance

class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)
        token['username'] = 'wx_{0}'.format(user.username)
        return token





    



