
from rest_framework import serializers
from a_bank.models import Bank,File,Batch

class BankSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
   
    class Meta:
        model = Bank
        fields = ['id',"name"]
        extra_kwargs = {'id': {'required': False}}

class FileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
   
    class Meta:
        model = File
        fields = ['id',"name","file_type","batch_id"]
        extra_kwargs = {'id': {'required': False}}
        
class BatchSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
   
    class Meta:
        model = Batch
        fields = ['id',"status","bank_id","store_path"]
        extra_kwargs = {'id': {'required': False}}

