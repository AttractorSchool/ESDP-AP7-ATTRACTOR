from django.db.models import Count, Max, Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, UpdateView

from notifications.models import Notifications


class NotificationsView(ListView):
    template_name = 'notifications.html'
    model = Notifications
    context_object_name = 'notifications'
    paginate_by = 15
    paginate_orphans = 0

    def get_queryset(self):
        queryset = Notifications.objects.filter(to_whom=self.kwargs['pk']).values(
            'to_whom',
            'from_whom',
            'type',
            'viewed',
            'message').\
            annotate(
            cnt=Count('viewed', filter=Q(viewed=False)),
            date=Max('created_at'),
            pk=Max('id'),
            response_pk=Max('response'),
        ).order_by('-date')
        return queryset


class NotificationsViewAsViewed(UpdateView):
    template_name = 'notifications.html'
    model = Notifications

    def get(self, request, *args, **kwargs):
        notification = get_object_or_404(Notifications, pk=kwargs['pk'])
        notification.viewed = True
        notification.save()
        return redirect('notifications', pk=request.user.pk)


class NotificationsViewAsUnviewed(UpdateView):
    template_name = 'notifications.html'
    model = Notifications

    def get(self, request, *args, **kwargs):
        notification = get_object_or_404(Notifications, pk=kwargs['pk'])
        notification.viewed = False
        notification.save()
        return redirect('notifications', pk=request.user.pk)
