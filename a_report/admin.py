from django.contrib import admin
from a_report.models import ReportByActivity, ReportByOperation, ReportByPerson, ReportByService,ReportBySuspicious
from a_report.models import Activity,Risk,PrecendentCrime,PersonType,ServiceType,OperationType

# Register your models here.

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

class ActivityAdmin(admin.ModelAdmin):
    list_display= ('code_ciiv','macro','activity',)


class PrecendentCrimeAdmin(admin.ModelAdmin):
    list_display= ('name','code')

class RiskAdmin(admin.ModelAdmin):
    list_display= ('name','code',)

admin.site.register(Activity,ActivityAdmin)
admin.site.register(Risk,RiskAdmin)
admin.site.register(PrecendentCrime,PrecendentCrimeAdmin)





admin.site.register(ServiceType)
admin.site.register(OperationType)
admin.site.register(PersonType)


admin.site.register(ReportByActivity,ReportByActivityAdmin)
admin.site.register(ReportByOperation,ReportByOperationAdmin)
admin.site.register(ReportByPerson,ReportByPersonAdmin)
admin.site.register(ReportByService,ReportByServiceAdmin)
admin.site.register(ReportBySuspicious,ReportBySuspiciousAdmin)