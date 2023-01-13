from django.contrib import admin
from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'id']


admin.site.register(Account, AccountAdmin)

