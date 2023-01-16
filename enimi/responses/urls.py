from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from responses.views.responses import StudentAddResponseView, TutorAddResponseView
from enimi.views import IndexView

urlpatterns = [
    path('<int:pk>/on_student/create/', StudentAddResponseView.as_view(), name='response_on_student'),
    path('<int:pk>/on_tutor/create/', TutorAddResponseView.as_view(), name='response_on_tutor'),
      # path('<int:pk>/data-to-responses/', GetDataForResponseView.as_view(), name='response_to_student',)

  ]
