from django.contrib import admin
from a_account.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display= ('username','company_name')
    exclude = ('password','groups','user_permissions','last_login')

admin.site.register(User,UserAdmin)



