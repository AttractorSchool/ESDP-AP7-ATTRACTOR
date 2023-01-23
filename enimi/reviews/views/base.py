from django.shortcuts import get_object_or_404, redirect
from django.views.generic import FormView, DetailView, ListView, TemplateView

from cabinet_tutors.models import TutorCabinets
from responses.models import Response
from reviews.forms import ReviewForm
from reviews.models.reviews import Review


class ReviewView(FormView):
    form_class = ReviewForm

    def post(self, request, *args, **kwargs):
        tutor = get_object_or_404(TutorCabinets, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)

        if form.is_valid():
            text = form.cleaned_data.get('text')
            user = request.user
            Review.objects.create(author=user, tutor=tutor, text=text)
        return redirect('student_on_tutor_review', pk=request.user.pk)

