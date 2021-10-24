

from django.contrib import admin
from a_bank.models import Bank, File, Batch, FileTypes
class BankAdmin(admin.ModelAdmin):
    list_display= ('name',)

class FileAdmin(admin.ModelAdmin):
    list_display= ('file_name',)

class FileTypesAdmin(admin.ModelAdmin):
    list_display= ('name',)

class BatchAdmin(admin.ModelAdmin):
    list_display= ('bank_id','status','create_on')






admin.site.register(Bank,BankAdmin)
admin.site.register(FileTypes,FileTypesAdmin)
admin.site.register(File,FileAdmin)
admin.site.register(Batch,BatchAdmin)


