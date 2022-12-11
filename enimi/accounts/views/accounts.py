from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.views.generic import CreateView

from accounts.forms import AccountForm
from accounts.models.accounts import Account


class AccountCreateView(CreateView):
    template_name = 'account_register.html'
    model = Account
    form_class = AccountForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            account = form.save(commit=False)
            account.username = account.email
            account.type = kwargs['type']
            account.save()
            login(request, account)
            # if account.type == 'tutor':
            #     return redirect('tutor_module_register', pk=account.pk)
            # if account.type == 'study_center':
            #     return redirect('study_center_module_register', pk=account.pk)
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)


def logout_view(request):
    logout(request)
    return redirect('index')
