from django.contrib import admin

from cabinet_tutors.models import TutorCabinets


# Register your models here.
class TutorCabinetsAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', ]


admin.site.register(TutorCabinets, TutorCabinetsAdmin)
