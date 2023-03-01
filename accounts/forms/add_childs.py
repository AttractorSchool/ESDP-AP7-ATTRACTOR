from django import forms
from accounts.models import Account
from django.forms import TextInput


class ChildrenForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label='Имя *')
    last_name = forms.CharField(required=True, label='Фамилия *')
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'father_name', 'birthday', 'avatar')
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'father_name': 'Отчество',
                  'avatar': 'Фото на аватар *', 'phone': 'Контакный телефон', 'birthday': 'Дата рождения *'}

        widgets = {
            'birthday': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 250px; height: 26px;',
                'type': 'date'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # group_name = 'basic_users'
            # group = Group.objects.get(name=group_name)
            # user.groups.add(group)

        return user