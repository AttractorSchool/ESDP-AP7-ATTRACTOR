from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView

from api.serializers import ChatSerializer, CitySerializer, RegionSerializer
from cabinet_parents.models import City, Region
from chat.models import Chat
from notifications.messages import chats
from notifications.models import Notifications
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
        if author.type == 'tutor' and author == response.author and response.survey and response.survey.user.parent \
                and not response.survey.user.with_email:
            chats(response.survey.user.parent, author, response, child=response.survey.user)
        # Когда репетитор отправляет сообщение самостоятельному ученику (автор отклика - репетитор)
        if author.type == 'tutor' and author == response.author and response.survey and response.survey.user.with_email:
            chats(response.survey.user, author, response)
        # Когда репетитор отправляет сообщение ученику, при этом сообщение приходит родителю (автор отклика - ученик)
        if author.type == 'tutor' and author != response.author and response.author.parent \
                and not response.author.with_email:
            chats(response.author.parent, author, response, child=response.survey.user)
        # Когда репетитор отправляет сообщение самостоятельному ученику (автор отклика - ученик)
        if author.type == 'tutor' and author != response.author and response.author.with_email:
            chats(response.author, author, response)
        # Когда самостоятельный ученик отправляет сообщение репетитору (автор отклика - репетитор)
        if author.type == 'student' and author != response.author:
            chats(response.author, author, response)
        # Когда самостоятльный ученик отправляет сообщение репетитору (автор отклика - ученик)
        if author.type == 'student' and response.cabinet_tutor:
            chats(response.cabinet_tutor.user, author, response)
        # Когда ученик отправляет сообщение репетитору от лица родителя (автор отклика - репетитор)
        if author.type == 'parents' and not response.cabinet_tutor:
            chats(response.author, response.survey.user, response)
        # Когда ученик отправляет сообщение репетитору от лица родителя (автор отклика - ученик)
        if author.type == 'parents' and response.cabinet_tutor:
            chats(response.cabinet_tutor.user, response.author, response)
        return JsonResponse({'chats': 'Сообщение добавлено'})


class GetChat(View):
    def get(self, request, *args, **kwargs):
        objects = Chat.objects.filter(response_id=self.kwargs['pk'])
        serializer = ChatSerializer(objects, many=True)
        return JsonResponse(serializer.data, safe=False)


class GetNotifications(View):
    def get(self, request, *args, **kwargs):
        count = Notifications.objects.filter(to_whom=kwargs.get('pk'), viewed=False).count()
        return JsonResponse({'count': count}, safe=False)


class RegionsAPI(View):
    def get(self, request, *args, **kwargs):
        objects = Region.objects.all()
        serializer = RegionSerializer(objects, many=True)
        return JsonResponse(serializer.data, safe=False)


class CitiesAPI(View):
    def get(self, request, *args, **kwargs):
        objects = City.objects.filter(region_id=kwargs.get('pk'))
        serializer = CitySerializer(objects, many=True)
        return JsonResponse(serializer.data, safe=False)

