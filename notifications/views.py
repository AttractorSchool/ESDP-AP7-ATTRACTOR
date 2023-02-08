from django.db.models import Count, Max, Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, UpdateView

from notifications.models import Notifications
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class NotificationsView(LoginRequiredMixin,ListView):
    template_name = 'notifications.html'
    model = Notifications
    context_object_name = 'notifications'
    paginate_by = 15
    paginate_orphans = 0

    def get_queryset(self):
        queryset = Notifications.objects.filter(to_whom=self.kwargs['pk']).values('type', 'viewed', 'message'). \
            annotate(
            cnt=Count('viewed', filter=Q(viewed=False)),
            date=Max('created_at'),
            pk=Max('id'),
            response_pk=Max('response'),
            response_author_pk=Q(response__author__pk=self.kwargs['pk']),
        ).order_by('-date')
        contains_viewed = False
        contains_unviewed = False
        for obj in queryset:
            if obj.get('type') == 'chat' and not obj.get('viewed'):
                contains_unviewed = True
            elif obj.get('type') == 'chat' and obj.get('viewed'):
                contains_viewed = True
        self.extra_context = {
            'contains_viewed': contains_viewed,
            'contains_unviewed': contains_unviewed,
        }
        return queryset

    def get_context_data(self, **kwargs):
        context = super(NotificationsView, self).get_context_data(**kwargs)
        context['notifications_count'] = Notifications.objects.filter(to_whom=self.request.user).count()
        return context

    def dispatch(self, request, *args, **kwargs):
        notification = get_object_or_404(Notifications, pk=kwargs.get('pk'))
        if request.user.pk != notification.to_whom.pk:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class NotificationsViewAsViewed(LoginRequiredMixin,UpdateView):
    template_name = 'notifications.html'
    model = Notifications

    def get(self, request, *args, **kwargs):
        notification = get_object_or_404(Notifications, pk=kwargs['pk'])
        notification.viewed = True
        notification.save()
        return redirect('notifications', pk=request.user.pk)

    def dispatch(self, request, *args, **kwargs):
        notification = get_object_or_404(Notifications, pk=kwargs.get('pk'))
        if request.user.pk != notification.to_whom.pk:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class NotificationsViewAsUnviewed(LoginRequiredMixin,UpdateView):
    template_name = 'notifications.html'
    model = Notifications

    def get(self, request, *args, **kwargs):
        notification = get_object_or_404(Notifications, pk=kwargs['pk'])
        notification.viewed = False
        notification.save()
        return redirect('notifications', pk=request.user.pk)

    def dispatch(self, request, *args, **kwargs):
        notification = get_object_or_404(Notifications, pk=kwargs.get('pk'))
        if request.user.pk != notification.to_whom.pk:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
