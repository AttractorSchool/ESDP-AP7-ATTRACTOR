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
        queryset = Notifications.objects.order_by('-created_at').filter(to_whom=self.kwargs['pk'])
        return queryset


class NotificationsViewAsViewed(UpdateView):
    template_name = 'notifications.html'
    model = Notifications

    def get(self, request, *args, **kwargs):
        notification = get_object_or_404(Notifications, pk=kwargs['pk'])
        notification.viewed = True
        notification.save()
        print(notification.viewed)
        return redirect('notifications', pk=request.user.pk)


class NotificationsViewAsUnviewed(UpdateView):
    template_name = 'notifications.html'
    model = Notifications

    def get(self, request, *args, **kwargs):
        notification = get_object_or_404(Notifications, pk=kwargs['pk'])
        notification.viewed = False
        notification.save()
        print(notification.viewed)
        return redirect('notifications', pk=request.user.pk)
