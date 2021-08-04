
from rest_framework import serializers
from a_bank.models import Bank

#Newspaper
class BankSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
   
    class Meta:
        model = Bank
        fields = ['id',"name"]
        extra_kwargs = {'id': {'required': False}}
