from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView

from accounts.forms import AccountForm, LoginForm
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


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        next = request.GET.get('next')
        form_data = {} if not next else {'next': next}
        form = self.form(form_data)
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        next = form.cleaned_data.get('next', None)
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        if next:
            return redirect(next)
        return redirect('index')
