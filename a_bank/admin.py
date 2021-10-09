

from django.contrib import admin
from a_bank.models import Bank, File, Batch, FileTypes,Activity,Risk,PrecendentCrime

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

admin.site.register(Bank,BankAdmin)
admin.site.register(File,FileAdmin)
admin.site.register(FileTypes,FileTypesAdmin)
admin.site.register(Batch,BatchAdmin)
admin.site.register(Activity,ActivityAdmin)
admin.site.register(Risk,RiskAdmin)
admin.site.register(PrecendentCrime,PrecendentCrimeAdmin)
