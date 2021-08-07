

from django.contrib import admin
from a_bank.models import Bank, File, Batch

class BankAdmin(admin.ModelAdmin):
    list_display= ('name',)

class FileAdmin(admin.ModelAdmin):
    list_display= ('name',)

class BatchAdmin(admin.ModelAdmin):
    list_display= ('status',)

admin.site.register(Bank,BankAdmin)
admin.site.register(File,FileAdmin)
admin.site.register(Batch,BatchAdmin)