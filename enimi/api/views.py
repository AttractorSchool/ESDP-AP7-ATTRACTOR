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
        # Когда репетитор отправляет сообщение ученику, при этом сообщение приходит родителю (автор отклика - репетитор)
        if author.type == 'tutor' and author == response.author and response.survey and response.survey.user.parent:
            chats(response.survey.user.parent, author)
        # Когда репетитор отправляет сообщение самостоятельному ученику (автор отклика - репетитор)
        if author.type == 'tutor' and author == response.author and response.survey and not response.survey.user.parent:
            chats(response.survey.user, author)
        # Когда репетитор отправляет сообщение ученику, при этом сообщение приходит родителю (автор отклика - ученик)
        if author.type == 'tutor' and author != response.author and response.author.parent:
            chats(response.author.parent, author)
        # Когда репетитор отправляет сообщение самостоятельному ученику (автор отклика - ученик)
        if author.type == 'tutor' and author != response.author and not response.author.parent:
            chats(response.author, author)
        # Когда самостоятельный ученик отправляет сообщение репетитору (автор отклика - репетитор)
        if author.type == 'student' and author != response.author:
            chats(response.author, author)
        # Когда самостоятльный ученик отправляет сообщение репетитору (автор отклика - ученик)
        if author.type == 'student' and response.cabinet_tutor:
            chats(response.cabinet_tutor.user, author)
        # Когда ученик отправляет сообщение репетитору от лица родителя (автор отклика - репетитор)
        if author.type == 'parents' and not response.cabinet_tutor:
            chats(response.author, response.survey.user)
        # Когда ученик отправляет сообщение репетитору от лица родителя (автор отклика - ученик)
        if author.type == 'parents' and response.cabinet_tutor:
            chats(response.cabinet_tutor.user, response.author)
        return JsonResponse({'chats': 'Сообщение добавлено'})

        # user = author
        # # Когда репетитор отправляет сообщение ученику, при этом сообщение приходит родителю (автор отклика - рпетитор)
        # if response.survey and response.survey.user.parent and response.survey.user.parent != user:
        #     chats(response.survey.user.parent, user)
        # # Когда репетитор отправляет сообщение ученику, при этом сообщение приходит родителю (автор отклика - ученик)
        # if response.cabinet_tutor and response.cabinet_tutor.user == user and response.author.parent:
        #     chats(response.author.parent, user)
        # # Когда репетитор отправляет сообщение самостоятельному ученику (автор отклика - репетитор)
        # if response.survey and not response.survey.user.parent and response.survey != user:
        #     chats(response.survey.user, user)
        # # Когда репетитор отправляет сообщение самостоятельному ученику (автор отклика - ученик)
        # if response.cabinet_tutor and response.cabinet_tutor.user == user and not response.author.parent:
        #     chats(response.author, user)
        # return JsonResponse({'chats': 'Сообщение добавлено'})


class GetChat(View):
    def get(self, request, *args, **kwargs):
        objects = Chat.objects.filter(response_id=self.kwargs['pk'])
        serializer = ChatSerializer(objects, many=True)
        return JsonResponse(serializer.data, safe=False)
