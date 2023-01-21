from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView

from api.serializers import ChatSerializer
from chat.models import Chat
from notifications.messages import chats
from responses.models import Response


class AddMessage(APIView):
    def post(self, request, *args, **kwargs):
        message = request.data.get('message_text')
        if message == '':
            return JsonResponse({'error': 'Введите сообщение'}, status=400)
        response = Response.objects.get(pk=kwargs.get('pk'))
        author = request.user
        Chat.objects.create(response=response, message=message, author=author)
        user = author
        if response.survey and response.survey.user.parent and response.survey.user.parent != user:
            chats(response.survey.user.parent, user)
        if response.survey and not response.survey.user.parent and response.survey != user:
            chats(response.survey.user, user)
        if response.cabinet_tutor and response.cabinet_tutor.user == user and response.author.parent:
            chats(response.author.parent, user)
        if response.cabinet_tutor and response.cabinet_tutor.user == user and not response.author.parent:
            chats(response.author, user)
        return JsonResponse({'chats': 'Сообщение добавлено'})


class GetChat(View):
    def get(self, request, *args, **kwargs):
        objects = Chat.objects.filter(response_id=self.kwargs['pk'])
        serializer = ChatSerializer(objects, many=True)
        return JsonResponse(serializer.data, safe=False)
