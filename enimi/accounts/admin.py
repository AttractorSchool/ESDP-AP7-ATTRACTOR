from django.contrib import admin


from accounts.models import Account
from django.contrib import admin


class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'id']


admin.site.register(Account, AccountAdmin)
