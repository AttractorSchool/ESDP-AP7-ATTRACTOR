from django import forms
from chat.models import Chat
from django.forms import Textarea


class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ('message',)
        widgets = {
            'message': Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'placeholder': 'Добавьте сообщение',
                'class': 'border-0 border-top rounded',
                'style': 'outline:0px none transparent; overflow:auto; resize:none',
            })
        }

