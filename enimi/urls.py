"""enimi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from board_tutors_students.views.base import BoardTutorView, BoardStudentView
from enimi.views import IndexView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('auth/', include('accounts.urls')),
                  path('', IndexView.as_view(), name='index'),
                  path('cabinet_parents/', include('cabinet_parents.urls')),
                  path('cabinet_student/', include('cabinet_student.urls')),
                  path('cabinet_tutors/', include('cabinet_tutors.urls')),
                  path('schedule/', include("calendarapp.urls")),
                  path('verification/', include('verify_email.urls')),
                  path('board_tutors_students/', include('board_tutors_students.urls')),
                  path('responses/', include("responses.urls")),
                  path('chats/', include("chat.urls")),
                  path('api/', include("api.urls")),
                  path('notifications/', include("notifications.urls")),
                  path('payments/', include("payments.urls")),
                  path('ratings/', include("ratings.urls")),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
