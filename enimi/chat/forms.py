from django import forms
from chat.models import Chat


class ChatForm(forms.ModelForm):
    message = forms.CharField(max_length=3000, required=False, label='',
                              widget=forms.Textarea(attrs={'name': 'body', 'rows': 3, 'cols': 21}))
    class Meta:
        model = Chat
        fields = ('message',)

