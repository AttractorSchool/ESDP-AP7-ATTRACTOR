from django.urls import path
from chat.views.add_chat import ResponsesAddChatMessageView

urlpatterns = [
    path('<int:pk>/chat_messages/', ResponsesAddChatMessageView.as_view(), name='add_chat_message'),
]