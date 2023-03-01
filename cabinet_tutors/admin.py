from django.contrib import admin

from cabinet_tutors.models import TutorCabinets, MyStudent, Languages


# Register your models here.
class TutorCabinetsAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', ]


admin.site.register(TutorCabinets, TutorCabinetsAdmin)


class MyStudentAdmin(admin.ModelAdmin):
    list_display = ['student', 'student_id', 'tutor', 'tutor_id']


admin.site.register(MyStudent, MyStudentAdmin)


class LangAdmin(admin.ModelAdmin):
    list_display = ['name', ]


admin.site.register(Languages, LangAdmin)
