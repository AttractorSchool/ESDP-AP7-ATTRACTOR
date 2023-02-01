from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from accounts.models import Account
from cabinet_tutors.models import TutorCabinets
from reviews.models import Review


class OnMeReviewsView(LoginRequiredMixin, ListView):
    template_name = 'on_tutor_reviews.html'
    model = Review

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super(OnMeReviewsView, self).get_context_data(object_list=object_list, **kwargs)
        tutor_cabinet = TutorCabinets.objects.get(id=self.kwargs['pk'])

        on_tutor_reviews = Review.objects.filter(tutor_id=tutor_cabinet.user.pk)
        review_rate_list = []
        for review in on_tutor_reviews:
            review_rate_list.append(review.rate)
        if len(review_rate_list) > 0:
            middle_rate = sum(review_rate_list) / len(review_rate_list)
            context['middle_rate'] = round(middle_rate, 1)

        reviews_stats = Review.objects.filter(tutor_id=tutor_cabinet.user.pk)

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

            context['reviews_count'] = len(review_rate_list)
        context['reviews'] = reviews_stats
        context['on_tutor_reviews'] = '1'
        return context