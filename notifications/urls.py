from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from notifications.views import NotificationsView, NotificationsViewAsViewed, NotificationsViewAsUnviewed
from responses.views.responses import StudentAddResponseView, TutorAddResponseView, ParentAddResponseView
from enimi.views import IndexView

urlpatterns = [
    path('<int:pk>/', NotificationsView.as_view(), name='notifications'),
    path('set_viewed/<int:pk>/', NotificationsViewAsViewed.as_view(), name='notification_viewed'),
    path('set_unviewed/<int:pk>/', NotificationsViewAsUnviewed.as_view(), name='notification_unviewed')
]
