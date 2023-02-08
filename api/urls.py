from django.urls import path

from api.views import AddMessage, GetChat, GetNotifications, CitiesAPI

urlpatterns = [
    path('response/<int:pk>/add-message/', AddMessage.as_view(), name='add_message'),
    path('response/<int:pk>/get-chat/', GetChat.as_view(), name='get_chat'),
    path('get_notifications/user/<int:pk>/', GetNotifications.as_view(), name='get_chat'),
    path('cities/region/<int:pk>', CitiesAPI.as_view(), name='city'),
]
