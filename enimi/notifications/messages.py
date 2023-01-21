from notifications.models import Notifications, TypeChoices


def registration(account):
    message = f'Добро пожаловать в ENIMI, {account.first_name} {account.last_name}. Регистрация прошла успешно.'
    Notifications.objects.create(to_whom=account, type=TypeChoices.REGISTRATION, message=message)


def response_to_tutor(response, child):
    subjects = ', '.join([subject.__str__() for subject in response.subjects.all()])
    message = f'На Вас оставил отклик {child.first_name} {child.last_name}. Интересующие предметы: {subjects}'
    Notifications.objects.create(to_whom=response.cabinet_tutor.user, type=TypeChoices.RESPONSE, message=message)


def response_from_parent(response, child):
    subjects = ', '.join([subject.__str__() for subject in response.subjects.all()])
    message = f'Вы оставили отклик на репетитора' \
              f' {response.cabinet_tutor.user.first_name} {response.cabinet_tutor.user.last_name} от лица ребенка' \
              f' {child.first_name} {child.last_name}. Интересующие предметы: {subjects}.'
    Notifications.objects.create(to_whom=response.author.parent, type=TypeChoices.RESPONSE, message=message)


def response_from_student():
    pass


def chats(to_whom, from_whom):
    if from_whom.type == 'tutor':
        message = f'Вам сообщение от репетитора {from_whom.first_name} {from_whom.last_name}'
    if from_whom.type == 'student':
        message = f'Вам сообщение от студента {from_whom.first_name} {from_whom.last_name}'
    if from_whom.type == 'parents':
        message = f'Вам сообщение от {from_whom.first_name} {from_whom.last_name} (родитель ученика)'
    Notifications.objects.create(to_whom=to_whom, from_whom=from_whom, type=TypeChoices.CHAT, message=message)
