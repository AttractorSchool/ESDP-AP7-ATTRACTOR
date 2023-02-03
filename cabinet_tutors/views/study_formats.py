from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView, CreateView, DeleteView

from cabinet_parents.forms import TutorAreaForm, StudentAreaForm
from cabinet_parents.models import TutorArea, StudentArea
from cabinet_tutors.forms.study_formats import TutorStudyFormatsForm
from cabinet_tutors.models import TutorStudyFormats


class TutorStudyFormatsCreateView(CreateView):
    template_name = 'study_formats/study_formats_create.html'
    model = TutorStudyFormats
    form_class = TutorStudyFormatsForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TutorStudyFormatsCreateView, self).get_context_data(object_list=object_list, **kwargs)
        context['tutor_address_form'] = TutorAreaForm()
        context['student_address_form'] = StudentAreaForm()
        return context

    def post(self, request, *args, **kwargs):
        study_format_form = self.form_class(request.POST)
        tutor_address_form = TutorAreaForm(request.POST)
        student_address_form = StudentAreaForm(request.POST)
        if study_format_form.is_valid() and tutor_address_form.is_valid() and student_address_form.is_valid():
            study_format = study_format_form.save()
            study_format.tutors.add(request.user.tutor)

            tutor_address = tutor_address_form.save()
            tutor_address.tutors.add(study_format)

            student_address = student_address_form.save()
            student_address.tutors.add(study_format)
            print(student_address)

            study_format.save()
            return redirect('tutor_cabinet', pk=request.user.tutor.pk)
        context = {}
        context['tutor_address_form'] = tutor_address_form
        context['student_address_form'] = student_address_form
        context['form'] = study_format_form
        return self.render_to_response(context)


class TutorStudyFormatsUpdateView(UpdateView):
    template_name = 'study_formats/study_formats_create.html'
    model = TutorStudyFormats
    form_class = TutorStudyFormatsForm

    def get_context_data(self, *, object_list=None, **kwargs):
        tutor_area = self.request.user.tutor.study_formats.tutor_area
        student_area = self.request.user.tutor.study_formats.student_area
        print(student_area)
        context = super(TutorStudyFormatsUpdateView, self).get_context_data(object_list=object_list, **kwargs)
        context['tutor_address_form'] = TutorAreaForm(
            instance=(TutorArea.objects.filter(tutors=tutor_area.pk) if
                      TutorArea.objects.filter(tutors=tutor_area.pk) else None),
            initial={
                'tutor_region': tutor_area.tutor_region,
                'tutor_city': tutor_area.tutor_city,
                'tutor_district': tutor_area.tutor_district,
            })
        context['student_address_form'] = StudentAreaForm(
            instance=(StudentArea.objects.filter(tutors=student_area.pk) if
                      StudentArea.objects.filter(tutors=student_area.pk) else None),
            initial={
                'student_region': student_area.student_region,
                'student_city': student_area.student_city,
                'student_district': student_area.student_district,
            })
        return context

    def post(self, request, *args, **kwargs):
        study_format_form = self.form_class(request.POST, instance=get_object_or_404(self.model, pk=kwargs.get('pk')))
        tutor_address_form = TutorAreaForm(request.POST, instance=self.request.user.tutor.study_formats.tutor_area)
        student_address_form = StudentAreaForm(request.POST, instance=self.request.user.tutor.study_formats.student_area)
        if study_format_form.is_valid() and tutor_address_form.is_valid() and student_address_form.is_valid():
            tutor_address_form.save()
            student_address_form.save()
            study_format_form.save()
            return redirect('tutor_cabinet', pk=request.user.tutor.pk)
        context = {}
        context['tutor_address_form'] = tutor_address_form
        context['student_address_form'] = student_address_form
        context['form'] = study_format_form
        return self.render_to_response(context)


class TutorStudyFormatsDeleteView(DeleteView):
    model = TutorStudyFormats
    context_object_name = 'study_format'

    def get_success_url(self):
        self.request.user.tutor.study_formats.tutor_area.delete()
        return reverse('tutor_cabinet', kwargs={'pk': self.request.user.tutor.pk})
