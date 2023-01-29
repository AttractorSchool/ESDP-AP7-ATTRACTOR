from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, View, UpdateView
from chat.forms import ChatForm
from chat.models import Chat
from notifications.models import Notifications
from responses.models import Response


class ResponsesAddChatMessageView(UpdateView):
    model = Response
    template_name = 'response_chat.html'
    form_class = ChatForm

    def get(self, request, *args, **kwargs):
        self.extra_context = {
            'back_page': request.META.get('HTTP_REFERER')
        }
        notifications = Notifications.objects.filter(
            response_id=kwargs.get('pk'),
            to_whom=request.user,
            type='chat'
        )
        for notification in notifications:
            notification.viewed = True
            notification.save()
        return super(ResponsesAddChatMessageView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        message = request.POST['message']
        response = Response.objects.get(pk=kwargs['pk'])
        author = self.request.user
        Chat.objects.create(response=response, message=message, author=author)
        return redirect('add_chat_message', pk=kwargs['pk'])
