

from django.contrib import admin
from a_bank.models import Bank

class BankAdmin(admin.ModelAdmin):
    list_display= ('name',)

admin.site.register(Bank,BankAdmin)