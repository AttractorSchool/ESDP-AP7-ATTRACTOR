from django.contrib.auth import login, logout, authenticate, get_user_model, update_session_auth_hash
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView, UpdateView

from accounts.forms import AccountForm, LoginForm
from accounts.forms.accounts import PasswordChangeForm
from accounts.models.accounts import Account
from cabinet_tutors.models import TutorCabinets


class AccountCreateView(CreateView):
    template_name = 'account_register.html'
    model = Account
    form_class = AccountForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        user = request.user

        if form.is_valid():
            account = form.save(commit=False)
            account.type = kwargs['type']
            account.username = account.email
            account.save()
            login(request, account)
            if account.type == 'parents':
                # account.email = user.email.split("@")[0]+account.first_name+user.email.split("@")[1]
                # account.username = account.email
                # account.type = kwargs['type']
                # account.parent = user
                return redirect('parents_cabinet_detail',
                                pk=account.pk)  # после создания страницы кабинета установите свой редирект
            if account.type == 'tutor':
                tutor = TutorCabinets.objects.create(
                    user=account
                )
                return redirect('tutor_cabinet', pk=tutor.pk)  # после создания страницы кабинета установите свой редирект
            if account.type == 'parents':
                return redirect('index')  # после создания страницы кабинета установите свой редирект
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
        if user.type == 'tutor':
            return redirect('tutor_cabinet', pk=user.tutor.pk)
        if user.type == 'parents':
            return redirect('parents_cabinet_detail', pk=user.pk)
        return redirect('index')


class PasswordChangeView(UpdateView):
    template_name = 'change_password.html'
    model = get_user_model()
    form_class = PasswordChangeForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(self.request, user)
            login(request, user)
            if user.type == 'tutor':
                return redirect('tutor_cabinet', pk=get_object_or_404(TutorCabinets, user=user).pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)
