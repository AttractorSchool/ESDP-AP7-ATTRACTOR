from django import forms
from accounts.models import Account



class ChildrenForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'father_name', 'birthday')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # group_name = 'basic_users'
            # group = Group.objects.get(name=group_name)
            # user.groups.add(group)
        return user