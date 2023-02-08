from django.contrib import admin
from accounts.models import Account
from responses.models import Response


class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'id']


admin.site.register(Account, AccountAdmin)


class ResponseAdmin(admin.ModelAdmin):
    list_display = ['author', 'hello_message', 'survey']


admin.site.register(Response, ResponseAdmin)


