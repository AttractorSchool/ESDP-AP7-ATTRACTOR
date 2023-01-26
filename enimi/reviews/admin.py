from django.contrib import admin
from reviews.models.reviews import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'id', ]


admin.site.register(Review, ReviewAdmin)

