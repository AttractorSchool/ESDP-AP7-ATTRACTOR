from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView

from api.serializers import ChatSerializer
from chat.models import Chat
from responses.models import Response


class AddMessage(APIView):
    def post(self, request, *args, **kwargs):
        message = request.data.get('message_text')
        if message == '':
            return JsonResponse({'error': 'Введите сообщение'}, status=400)
        response = Response.objects.get(pk=kwargs.get('pk'))
        author = request.user
        Chat.objects.create(response=response, message=message, author=author)
        return JsonResponse({'chats': 'Сообщение добавлено'})


class GetChat(View):
    def get(self, requesr, *args, **kwargs):
        objects = Chat.objects.filter(response_id=self.kwargs['pk'])
        serializer = ChatSerializer(objects, many=True)
        return JsonResponse(serializer.data, safe=False)
