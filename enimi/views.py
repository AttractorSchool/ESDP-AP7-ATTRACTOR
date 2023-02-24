from accounts.models.accounts import UserCategoryChoices
from django.db.models import Count, Exists, OuterRef
from django.views.generic import TemplateView
from reviews.models import Review
from accounts.models import Account
from cabinet_tutors.models import MyStudent

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        reviews = Review.objects.all().order_by('review_date')
        review_context = [review for review in reviews]
        review_context = review_context[0:4]

        # tutors = Account.objects.filter()
        # popular_reviews = Review.objects.all().order_by('-rate')
        # popular_review_context = [review for review in popular_reviews]
        # popular_review_context = popular_review_context[0:4]

        # popular_tutors = Account.objects.annotate(
        #     num_students=Count('students')
        # ).filter(
        #     Exists(MyStudent.objects.filter(student=OuterRef('pk')))
        # ).order_by('-num_students')
        # print(popular_tutors)

        popular_tutors = Account.objects.filter(type='tutor').annotate(num_students=Count('students'))\
            .order_by('-num_students')[0:3]
        print(popular_tutors)
        context['popular_tutors'] = popular_tutors
        context['reviews'] = review_context
        context['types'] = UserCategoryChoices.choices
        return context

