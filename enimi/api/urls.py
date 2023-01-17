from django.urls import path

from api.views import AddMessage, GetChat

urlpatterns = [
    path('response/<int:pk>/add-message/', AddMessage.as_view(), name='add_message'),
    path('response/<int:pk>/get-chat/', GetChat.as_view(), name='get_chat'),
]
