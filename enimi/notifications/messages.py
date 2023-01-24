from notifications.models import Notifications, TypeChoices


def registration(account):
    message = f'Добро пожаловать в ENIMI, {account.first_name} {account.last_name}. Регистрация прошла успешно.'
    Notifications.objects.create(to_whom=account, type=TypeChoices.REGISTRATION, message=message)


def response_from_tutor_to_student(response, student):
    subjects = ', '.join([subject.__str__() for subject in response.subjects.all()])
    message = f'На Вас оставил отклик репетитор {response.author.first_name} {response.author.last_name}. ' \
              f'Предлагаемые предметы: {subjects}'
    Notifications.objects.create(to_whom=student, type=TypeChoices.RESPONSE, message=message)


def response_from_tutor_to_student_with_parent(response, student):
    subjects = ', '.join([subject.__str__() for subject in response.subjects.all()])
    message = f'На анкету {student.first_name} {student.last_name} оставил отклик репетитор ' \
              f'{response.author.first_name} {response.author.last_name}. ' \
              f'Предлагаемые предметы: {subjects}'
    Notifications.objects.create(to_whom=student.parent, type=TypeChoices.RESPONSE, message=message)


def response_from_tutor_to_self(response, student):
    subjects = ', '.join([subject.__str__() for subject in response.subjects.all()])
    message = f'Вы оставили отклик на {student.first_name} {student.last_name}. Предлагаемые предметы: {subjects}'
    Notifications.objects.create(to_whom=response.author, type=TypeChoices.RESPONSE, message=message)


def response_from_student_to_tutor(response, tutor):
    subjects = ', '.join([subject.__str__() for subject in response.subjects.all()])
    message = f'На Вас оставил отклик {response.author.first_name} {response.author.last_name}. ' \
              f'Интересующие предметы: {subjects}'
    Notifications.objects.create(to_whom=tutor, type=TypeChoices.RESPONSE, message=message)


def response_from_student_to_self(response, tutor):
    subjects = ', '.join([subject.__str__() for subject in response.subjects.all()])
    message = f'Вы оставили отклик на репетитора {tutor.first_name} {tutor.last_name}. ' \
              f'Интересующие предметы: {subjects}'
    Notifications.objects.create(to_whom=response.author, type=TypeChoices.RESPONSE, message=message)


def response_to_parent_from_self(response, child, tutor):
    subjects = ', '.join([subject.__str__() for subject in response.subjects.all()])
    message = f'Вы оставили отклик на репетитора' \
              f' {tutor.first_name} {tutor.last_name} от лица ребенка' \
              f' {child.first_name} {child.last_name}. Интересующие предметы: {subjects}.'
    Notifications.objects.create(to_whom=response.author.parent, type=TypeChoices.RESPONSE, message=message)


def chats(to_whom, from_whom):
    if from_whom.type == 'tutor':
        message = f'Сообщения от репетитора {from_whom.first_name} {from_whom.last_name}'
    if from_whom.type == 'student' and from_whom.with_email:
        message = f'Сообщения от студента {from_whom.first_name} {from_whom.last_name}'
    if from_whom.type == 'student' and not from_whom.with_email:
        message = f'Сообщения от {from_whom.first_name} {from_whom.last_name} (родитель ученика)'
    Notifications.objects.create(to_whom=to_whom, from_whom=from_whom, type=TypeChoices.CHAT, message=message)
