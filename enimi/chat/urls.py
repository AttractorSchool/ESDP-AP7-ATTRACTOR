from django.urls import path
from chat.views.add_chat import ResponsesAddChatMessageView

urlpatterns = [
    path('response/<int:pk>/', ResponsesAddChatMessageView.as_view(), name='add_chat_message'),
]