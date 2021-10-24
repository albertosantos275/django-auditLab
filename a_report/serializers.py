
from rest_framework import serializers
from a_report.models import ReportByActivity, ReportByOperation, ReportByPerson, ReportByService, ReportBySuspicious


       
class ReportByActivitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    risk_name = serializers.SerializerMethodField('_risk_name')
    precendent_crime_name = serializers.SerializerMethodField('_precendent_crime')

    def _risk_name(self, ReportByActivity):
      return ReportByActivity.risk_id.name      

    def _precendent_crime(self, ReportByActivity):
      return ReportByActivity.precendent_crime_id.name  
    
    class Meta:
        model = ReportByActivity
        fields = ['id',"batch_id",'risk_name',"precendent_crime_id",'risk_name','risk_id','total']
        extra_kwargs = {'id': {'required': False}}




class ReportByOperationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    operation_name = serializers.SerializerMethodField('_operation_name')

    def _operation_name(self, ReportByOperation):
      return ReportByOperation.operation_id.name  

    class Meta:
        model = ReportByOperation
        fields = ['id',"batch_id",'operation_id',"operation_name",'total']
        extra_kwargs = {'id': {'required': False}}


class ReportByPersonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    person_type_name = serializers.SerializerMethodField('_person_type_name')

    def _person_type_name(self, ReportByPerson):
      return ReportByPerson.person_type_id.name  

    class Meta:
        model = ReportByPerson
        fields = ['id',"batch_id",'person_type_id','person_type_name',"risk",'total']
        extra_kwargs = {'id': {'required': False}}



class ReportByServiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    service_type_name = serializers.SerializerMethodField('_service_type_name')

    def _service_type_name(self, ReportByService):
      return ReportByService.service_type_id.name  

    class Meta:
        model = ReportByService
        fields = ['id',"batch_id",'service_type_id','service_type_name',"phase",'total']
        extra_kwargs = {'id': {'required': False}}


class ReportBySuspiciousSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    activity_name = serializers.SerializerMethodField('_activity_name')

    def _activity_name(self, ReportBySuspicious):
      return ReportBySuspicious.activity_id.name  

    class Meta:
        model = ReportBySuspicious
        fields = ['id',"batch_id",'activity_id','activity_name','transaction_id',"lastname",'name','avg_o_act_avg','total_o_act_avg','transactions','total']
        extra_kwargs = {'id': {'required': False}}