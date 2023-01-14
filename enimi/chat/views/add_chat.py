from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, View
from chat.forms import ChatForm
from chat.models import Chat
from responses.models import Response

class ResponsesAddChatMessageView(CreateView):
    model = Chat
    template_name = 'response_chat.html'
    form_class = ChatForm

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(kwargs['pk'])
        message = request.POST['message']
        response = Response.objects.get(pk=kwargs['pk'])
        author = self.request.user
        Chat.objects.create(response=response, message=message, author=author)
        return redirect('add_chat_message', pk=kwargs['pk'])

    def get_context_data(self, **kwargs):
        print("JKKKKKK")
        context = super().get_context_data(**kwargs)
        context['form'] = ChatForm()
        context['chats'] = Chat.objects.filter(response_id=self.kwargs['pk'])
        return context



