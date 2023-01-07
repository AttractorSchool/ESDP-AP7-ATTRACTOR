from django.contrib import admin
from cabinet_parents.models import City
from cabinet_parents.models import District
from cabinet_parents.models import Program
from cabinet_parents.models import EducationTime
from cabinet_parents.models import OnlinePlatform
from cabinet_parents.models import Region
from cabinet_parents.models import StudentArea
from cabinet_parents.models import TutorArea
from cabinet_parents.models import Subject
from cabinet_parents.models import Survey
from cabinet_parents.models import Test


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'created_at', 'updated_at')
    list_filter = ('city', )
    search_fields = ('city',)
    fields = ('id', 'city', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(City, CityAdmin)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'district', 'created_at', 'updated_at')
    list_filter = ('district', )
    search_fields = ('district',)
    fields = ('id', 'district', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(District, DistrictAdmin)

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'program', 'created_at', 'updated_at')
    list_filter = ('program', )
    search_fields = ('program',)
    fields = ('id', 'program', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(Program, ProgramAdmin)

class EducationTimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'education_time', 'created_at', 'updated_at')
    list_filter = ('education_time', )
    search_fields = ('education_time',)
    fields = ('id', 'education_time', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(EducationTime, EducationTimeAdmin)


class OnlinePlatformAdmin(admin.ModelAdmin):
    list_display = ('id', 'online_platform', 'created_at', 'updated_at')
    list_filter = ('online_platform',)
    search_fields = ('online_platform',)
    fields = ('id', 'online_platform', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(OnlinePlatform, OnlinePlatformAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'region', 'created_at', 'updated_at')
    list_filter = ('region', )
    search_fields = ('region',)
    fields = ('id', 'region', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Region, RegionAdmin)


class StudentAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey', 'student_region', 'student_city', 'student_district', 'created_at', 'updated_at')
    list_filter = ('survey', 'student_region', 'student_city', 'student_district')
    search_fields = ('survey', 'student_region', 'student_city', 'student_district')
    fields = ('id', 'survey', 'student_region', 'student_city', 'student_district', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(StudentArea, StudentAreaAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'created_at', 'updated_at')
    list_filter = ('subject',)
    search_fields = ('subject',)
    fields = ('id', 'subject', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Subject, SubjectAdmin)


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'education_time', 'min_cost','max_cost', 'tutor_area','student_area','is_active','is_deleted', 'created_at', 'changed_at')
    list_filter = ('user', 'education_time', 'min_cost','max_cost', 'tutor_area','student_area','is_active',)
    search_fields = ('user',  'education_time', 'min_cost','max_cost', 'tutor_area','student_area','is_active','is_deleted', 'created_at', 'changed_at')
    fields = ('id', 'user', 'education_time', 'min_cost','max_cost', 'tutor_area','student_area','is_active','is_deleted', 'created_at', 'changed_at')
    readonly_fields = ('id', 'created_at', 'changed_at')


admin.site.register(Survey, SurveyAdmin)


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_name', 'created_at', 'updated_at')
    list_filter = ('test_name', )
    search_fields = ('test_name',)
    fields = ('id', 'test_name', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Test, TestAdmin)


class TutorAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tutor_region', 'tutor_city', 'tutor_district', 'created_at', 'updated_at')
    list_filter = ('tutor_region', 'tutor_city', 'tutor_district')
    search_fields = ('tutor_region', 'tutor_city', 'tutor_district')
    fields = ('id', 'tutor_region', 'tutor_city', 'tutor_district', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(TutorArea, TutorAreaAdmin)
