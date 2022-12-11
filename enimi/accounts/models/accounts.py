from django.db.models import TextChoices


class UserCategoryChoices(TextChoices):
    STUDY_CENTER = 'study_center', 'Учебный центр'
    STUDENT = 'student', 'Ученик'
    TUTOR = 'tutor', 'Репетитор'
    PARENTS = 'parents', 'Родители'