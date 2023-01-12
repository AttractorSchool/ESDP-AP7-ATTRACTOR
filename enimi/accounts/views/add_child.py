from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from accounts.forms import ChildrenForm
from accounts.models import Account


class AddChildView(CreateView):
    template_name = 'add_child.html'
    model = Account
    form_class = ChildrenForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            child = form.save(commit=False)
            child.email = user.email.split("@")[0] + child.first_name + '@' + user.email.split("@")[1]
            child.username = child.email
            child.parent = Account.objects.get(pk=kwargs['pk'])
            child.save()
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('index')
