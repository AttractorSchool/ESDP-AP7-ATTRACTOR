from django.urls import reverse
from django.views.generic import CreateView, DeleteView

from cabinet_tutors.forms.subjects_and_costs import SubjectsAndCostsForm, SubjectsAndCostsFormSet
from cabinet_tutors.models import SubjectsAndCosts


class SubjectsAndCostCreateUpdateView(CreateView):
    template_name = 'subjects_and_costs/subjects_and_costs_create_or_update.html'
    form_class = SubjectsAndCostsForm
    model = SubjectsAndCosts

    def get_context_data(self, **kwargs):
        context = super(SubjectsAndCostCreateUpdateView, self).get_context_data(**kwargs)
        context['formset'] = SubjectsAndCostsFormSet(
            queryset=SubjectsAndCosts.objects.filter(tutors=self.request.user.tutor).order_by('id'))
        return context

    def post(self, request, *args, **kwargs):
        formset = SubjectsAndCostsFormSet(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)
        else:
            context = {}
            context['errors'] = formset.errors
            context['formset'] = SubjectsAndCostsFormSet(
                queryset=SubjectsAndCosts.objects.filter(tutors=self.request.user.tutor).order_by('id'))
        return self.render_to_response(context)

    def form_valid(self, formset):
        subjects_and_costs = formset.save(commit=False)
        for subject_and_cost in subjects_and_costs:
            subject_and_cost.save()
            self.request.user.tutor.subjects_and_costs.add(subject_and_cost)
        return super().form_valid(formset)

    def get_success_url(self):
        return reverse('tutor_cabinet', kwargs={'pk': self.request.user.tutor.pk})


class SubjectsAndCostDeleteView(DeleteView):
    model = SubjectsAndCosts
    context_object_name = 'subjects_and_costs'

    def get_success_url(self):
        return reverse('tutor_cabinet', kwargs={'pk': self.request.user.tutor.pk})
