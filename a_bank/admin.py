

from django.contrib import admin
from a_bank.models import Bank, File, Batch, FileTypes, Activity, Risk, PrecendentCrime, ReportByActivity, ReportByOperation, ReportByPerson, ReportByService, ServiceType, OperationType,PersonType,ReportBySuspicious

class BankAdmin(admin.ModelAdmin):
    list_display= ('name',)

class FileAdmin(admin.ModelAdmin):
    list_display= ('file_name',)

class FileTypesAdmin(admin.ModelAdmin):
    list_display= ('name',)

class BatchAdmin(admin.ModelAdmin):
    list_display= ('bank_id','status','create_on')

class ActivityAdmin(admin.ModelAdmin):
    list_display= ('code_ciiv','macro','activity',)


class PrecendentCrimeAdmin(admin.ModelAdmin):
    list_display= ('name','code')

class RiskAdmin(admin.ModelAdmin):
    list_display= ('name','code',)


class ReportByActivityAdmin(admin.ModelAdmin):
    list_display= ('batch_id','precendent_crime_id','risk_id',)

class ReportByOperationAdmin(admin.ModelAdmin):
    list_display= ('operation_id',)  

class ReportByPersonAdmin(admin.ModelAdmin):
    list_display= ('person_type_id',)  


class ReportByServiceAdmin(admin.ModelAdmin):
    list_display= ('service_type_id',)  

class ReportBySuspiciousAdmin(admin.ModelAdmin):
    list_display= ('transaction_id','name','lastname')  


admin.site.register(Bank,BankAdmin)
admin.site.register(FileTypes,FileTypesAdmin)
admin.site.register(File,FileAdmin)
admin.site.register(Batch,BatchAdmin)
admin.site.register(Activity,ActivityAdmin)
admin.site.register(Risk,RiskAdmin)
admin.site.register(PrecendentCrime,PrecendentCrimeAdmin)



admin.site.register(ReportByActivity,ReportByActivityAdmin)
admin.site.register(ReportByOperation,ReportByOperationAdmin)
admin.site.register(ReportByPerson,ReportByPersonAdmin)
admin.site.register(ReportByService,ReportByServiceAdmin)
admin.site.register(ReportBySuspicious,ReportBySuspiciousAdmin)

admin.site.register(ServiceType)
admin.site.register(OperationType)
admin.site.register(PersonType)

