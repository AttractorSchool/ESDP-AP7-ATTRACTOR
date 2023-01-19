from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, View, UpdateView
from chat.forms import ChatForm
from chat.models import Chat
from responses.models import Response


class ResponsesAddChatMessageView(UpdateView):
    model = Response
    template_name = 'response_chat.html'
    form_class = ChatForm

    def post(self, request, *args, **kwargs):
        message = request.POST['message']
        response = Response.objects.get(pk=kwargs['pk'])
        author = self.request.user
        Chat.objects.create(response=response, message=message, author=author)
        return redirect('add_chat_message', pk=kwargs['pk'])
