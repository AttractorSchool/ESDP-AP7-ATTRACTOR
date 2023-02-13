import datetime

from django.db.models import Q, Avg, Max, Count, Min
from django.db.models.functions import Round
from django.views.generic import ListView, DetailView

from cabinet_parents.models import Subject
from cabinet_parents.models import Survey, City
from cabinet_tutors.models import TutorCabinets, SubjectsAndCosts
from reviews.models import Review


class BoardStudentView(ListView):
    template_name = 'board_student.html'
    model = Survey
    context_object_name = 'surveys'

    def get(self, request, *args, **kwargs):
        self.min_cost = request.GET.get("min_cost")
        self.max_cost = request.GET.get("max_cost")
        self.subject = request.GET.get("subject")
        self.city = request.GET.get("city")
        self.format = request.GET.get("format")
        self.order = request.GET.get("order")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['subjects'] = Subject.objects.all()
        context['cities'] = City.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.city and self.format == "student":
            queryset = queryset.filter(student_area__student_city__in=self.city)
        if self.city and self.format == "tutor":
            queryset = queryset.filter(tutor_area__tutor_city__in=self.city)
        if self.min_cost and self.max_cost:
            queryset = queryset.filter(
                (Q(min_cost__gte=self.min_cost) & Q(max_cost__lte=self.max_cost)) |
                (Q(min_cost__lte=self.max_cost) & Q(max_cost__gte=self.min_cost))
            )
        else:
            if self.max_cost:
                queryset = queryset.filter(Q(min_cost__lte=self.max_cost) | Q(max_cost__lte=self.max_cost))
            if self.min_cost:
                queryset = queryset.filter(Q(min_cost__gte=self.min_cost) | Q(max_cost__gte=self.min_cost))
        if self.subject:
            queryset = queryset.filter(subjects=self.subject)
        if self.order == "by_cost_up":
            queryset = queryset.order_by('min_cost', 'max_cost')
        if self.order == "by_cost_down":
            queryset = queryset.order_by('-min_cost', '-max_cost')
        return queryset


class BoardTutorView(ListView):
    template_name = 'board_tutor.html'
    model = TutorCabinets
    context_object_name = 'tutors'

    def get(self, request, *args, **kwargs):
        self.min_cost = request.GET.get("min_cost")
        self.max_cost = request.GET.get("max_cost")
        self.subject = request.GET.get("subject")
        self.city = request.GET.get("city")
        self.format = request.GET.get("format")
        self.order = request.GET.get("order")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['subjects'] = Subject.objects.all()
        context['cities'] = City.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset().order_by("user__services__status", "-user__services__start_date")
        queryset = queryset. \
            exclude(gender=None).exclude(languages=None). \
            exclude(about=None). \
            exclude(education=None). \
            exclude(subjects_and_costs=None). \
            exclude(study_formats=None)
        if self.city and self.format == "student":
            queryset = queryset.filter(study_formats__student_area__student_city__in=self.city)
        if self.city and self.format == "tutor":
            queryset = queryset.filter(study_formats__tutor_area__tutor_city__in=self.city)
        if self.subject:
            queryset = TutorCabinets.objects.filter(subjects_and_costs__subject__in=self.subject)
        if self.min_cost and self.max_cost:
            subjects = SubjectsAndCosts.objects.filter(
                (Q(cost__gte=self.min_cost) & Q(cost__lte=self.max_cost)) |
                (Q(cost__lte=self.max_cost) & Q(cost__gte=self.min_cost)))
            queryset = TutorCabinets.objects.filter(subjects_and_costs__in=subjects)
        else:
            if self.max_cost:
                subjects = SubjectsAndCosts.objects.filter(cost__lte=self.max_cost)
                queryset = TutorCabinets.objects.filter(subjects_and_costs__in=subjects)
            if self.min_cost:
                subjects = SubjectsAndCosts.objects.filter(cost__gte=self.min_cost)
                queryset = TutorCabinets.objects.filter(subjects_and_costs__in=subjects)
        queryset = queryset.annotate(
            avg_rate=Round(Avg('user__reviews_to__rate'), 1),
            reviews_count=Count('user__reviews_to', distinct=True),
            max_experience=Max('subjects_and_costs__experience'),
            most_min_cost=(Min('subjects_and_costs__cost')),
            most_max_cost=(Max('subjects_and_costs__cost'))
        )
        if self.order == "by_cost_up":
            queryset = queryset.order_by('most_min_cost')
        if self.order == "by_cost_down":
            queryset = queryset.order_by('-most_max_cost')
        return queryset


class TutorBoardDetailPageView(DetailView):
    template_name = 'tutor_board_detail_page.html'
    model = TutorCabinets
    context_object_name = 'tutor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tutor = TutorCabinets.objects.get(id=self.object.pk)
        on_tutor_reviews = Review.objects.filter(tutor=tutor.user)
        review_rate_list = []
        for review in on_tutor_reviews:
            review_rate_list.append(review.rate)
        if len(review_rate_list) > 0:
            middle_rate = sum(review_rate_list) / len(review_rate_list)
            context['middle_rate'] = round(middle_rate, 1)

        cost_list = []
        costs = SubjectsAndCosts.objects.filter(tutors=self.object)
        exp = SubjectsAndCosts.objects.filter(tutors=self.object).order_by('-experience').first()
        print(exp)
        experience = exp.experience
        for cost in costs:
            cost_list.append(cost.cost)
        if len(cost_list) > 0:
            middle_cost = round(sum(cost_list) / len(cost_list))
            context['middle_cost'] = middle_cost
        educations = tutor.education.all()

        reviews = Review.objects.filter(tutor_id=tutor.user.pk)

        reviews_stats = Review.objects.filter(tutor_id=tutor.user.pk)
        if reviews_stats:
            five_sum = []
            four_sum = []
            three_sum = []
            two_sum = []
            one_sum = []
            for rate in reviews_stats:
                if rate.rate == 5:
                    five_sum.append(rate.rate)
                if rate.rate == 4:
                    four_sum.append(rate.rate)
                if rate.rate == 3:
                    three_sum.append(rate.rate)
                if rate.rate == 2:
                    two_sum.append(rate.rate)
                if rate.rate == 1:
                    one_sum.append(rate.rate)
            five_sum = len(five_sum)
            four_sum = len(four_sum)
            three_sum = len(three_sum)
            two_sum = len(two_sum)
            one_sum = len(one_sum)
            summary_rate = five_sum + four_sum + three_sum + two_sum + one_sum
            proportion_five_sum = five_sum * 100 / summary_rate
            proportion_four_sum = four_sum * 100 / summary_rate
            proportion_three_sum = three_sum * 100 / summary_rate
            proportion_two_sum = two_sum * 100 / summary_rate
            proportion_one_sum = one_sum * 100 / summary_rate

            context['proportion_five_sum'] = round(proportion_five_sum)
            context['proportion_four_sum'] = round(proportion_four_sum)
            context['proportion_three_sum'] = round(proportion_three_sum)
            context['proportion_two_sum'] = round(proportion_two_sum)
            context['proportion_one_sum'] = round(proportion_one_sum)

            context['five_sum'] = five_sum
            context['four_sum'] = four_sum
            context['three_sum'] = three_sum
            context['two_sum'] = two_sum
            context['one_sum'] = one_sum

        context['tutor'] = tutor
        context['reviews'] = on_tutor_reviews
        context['reviews_count'] = len(review_rate_list)
        context['educations'] = educations
        context['experience'] = experience
        context['reviews'] = reviews

        return context


class StudentBoardDetailPageView(DetailView):
    template_name = 'student_board_detail_page.html'
    model = Survey
    context_object_name = 'survey'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        survey = Survey.objects.get(id=self.kwargs['pk'])
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        if survey.user.birthday:
            delta = int(now[0:4]) - int(survey.user.birthday[0:4])
            context['age'] = delta
        else:
            context['age'] = ""
        return context
