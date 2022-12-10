from django.http import HttpResponse
from django.views.generic import TemplateView


class ExampleView(TemplateView):
    template_name = 'example_index.html'
