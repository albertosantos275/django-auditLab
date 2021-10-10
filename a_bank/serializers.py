
from rest_framework import serializers
from a_bank.models import Bank,File,Batch,FileTypes

class BankSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
   
    class Meta:
        model = Bank
        fields = ['id',"name"]
        extra_kwargs = {'id': {'required': False}}


class FileTypesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
   
    class Meta:
        model = FileTypes
        fields = ['id',"name","code"]
        extra_kwargs = {'id': {'required': False}}



class FileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
   
    class Meta:
        model = File
        fields = ['id',"name","batch_id"]
        extra_kwargs = {'id': {'required': False}}
        
class BatchSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    file_type_name = serializers.SerializerMethodField('_file_type_name')
    file_type_code = serializers.SerializerMethodField('_file_type_code')
    bank_name= serializers.SerializerMethodField('_bank_name')

    def _file_type_name(self, Batch):
      return Batch.file_type_id.name      

    def _file_type_code(self, Batch):
      return Batch.file_type_id.code  
    
    def _bank_name(self, Batch):
      return Batch.bank_id.name 
   
    class Meta:
        model = Batch
        fields = ['id',"status","bank_id",'file_type_id','file_type_name','file_type_code','bank_name','number_files_submitted']
        extra_kwargs = {'id': {'required': False}}

