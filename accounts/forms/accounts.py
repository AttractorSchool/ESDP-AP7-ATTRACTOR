from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms import TextInput
from accounts.models.accounts import Account


class AccountForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label='Имя *')
    last_name = forms.CharField(required=True, label='Фамилия *')
    password = forms.CharField(label='Пароль *', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль *', strip=False, required=True,
                                       widget=forms.PasswordInput)

    phone = forms.CharField(label='Номер телефона *')
    email = forms.CharField(label='Email *')

    class Meta:
        model = Account

        fields = (
            'first_name', 'last_name', 'father_name', 'email', 'phone', 'birthday', 'avatar', 'password',
            'password_confirm'
        )
        widgets = {
            'birthday': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 250px; height: 26px;',
                'type': 'date'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
            # group_name = 'basic_users'
            # group = Group.objects.get(name=group_name)
            # user.groups.add(group)
        return user


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label="Новый пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label="Старый пароль", strip=False, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['password', 'password_confirm', 'old_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неправильный!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.EmailField(required=True, label='Email *')
    password = forms.CharField(required=True, label='Password *', widget=forms.PasswordInput)
    next = forms.CharField(required=False, widget=forms.HiddenInput)


class AvatarForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('avatar',)


class UserWithoutEmailUpdateForm(forms.ModelForm):
    # first_name = forms.CharField(required=True, label='Имя *')
    # last_name = forms.CharField(required=True, label='Фамилия *')
    class Meta:
        model = get_user_model()
        fields = ('avatar', 'birthday', )
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'father_name': 'Отчество',
                  'avatar': 'Фотография в профиле', 'birthday': 'Дата рождения'}
        widgets = {
            'birthday': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 250px; height: 26px;',
                'type': 'date'
            }),
        }


class UserUpdateForm(forms.ModelForm):
    # first_name = forms.CharField(required=True, label='Имя *')
    # last_name = forms.CharField(required=True, label='Фамилия *')
    email = forms.EmailField(required=True, label='Email')
    class Meta:
        model = get_user_model()
        fields = ('avatar', 'phone', 'email', 'birthday', )
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'father_name': 'Отчество',
                  'avatar': 'Фото на аватар', 'phone': 'Телефон', 'email': 'Email', 'birthday': 'Дата рождения'}

        widgets = {
            'birthday': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 250px; height: 26px;',
                'type': 'date'
            }),
        }
