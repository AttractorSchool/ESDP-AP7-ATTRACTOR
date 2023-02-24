import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView
from rest_framework.views import APIView
from payments.models import Service, Order, ServiceStatus
from payments.models.orders import OrderStatusChoices
from payments.models.services_status import ServiceStatusChoices
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class SelectServiceView(LoginRequiredMixin,ListView):
    model = Service
    template_name = 'service_selection_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Service.objects.all()
        context['services'] = services
        return context

class ServiceDetailView(LoginRequiredMixin,DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'

    def get(self, request, *args, **kwargs):
        self.extra_context = {
            'back_page': request.META.get('HTTP_REFERER')
        }
        return super(ServiceDetailView, self).get(request, *args, **kwargs)

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_superuser or not request.user.type == "tutor":
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)

class OrderOnServiceCreateView(LoginRequiredMixin,CreateView):
    model = Service
    template_name = 'order_to_pay.html'

    def post(self, request, *args, **kwargs):
        service = Service.objects.get(id=kwargs['pk'])
        order = Order.objects.create(email=request.user.email, amount=service.price,
                                     description=service.description, status=OrderStatusChoices.NOT_PAID,
                                     service=service, user=request.user)
        context = {}
        context['order'] = order
        return self.render_to_response(context)

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_superuser or not request.user.type == "tutor":
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


class OrderStatusUpdateView(LoginRequiredMixin,UpdateView):
    model = Order

    def post(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs['pk'])
        order.status = OrderStatusChoices.PAID
        order.save()
        start_date = datetime.datetime.now()
        end_date = start_date + datetime.timedelta(days=order.service.duration)
        # end_date = datetime.datetime.strptime(end_date, '%m-%d-%y %H:%M:%S')
        service_status = ServiceStatus.objects.create(user_id=request.user.pk,
                                                      service_id=order.service.pk,
                                                      status=ServiceStatusChoices.ACTIVE,
                                                      start_date=start_date, end_date=end_date,
                                                      order=order)
        service_status.save()
        return HttpResponse(status=200)
        # return redirect('orders_list')

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_superuser or not request.user.type == "tutor":
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


class OrdersListView(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'orders_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrdersListView, self).get_context_data(object_list=object_list, **kwargs)
        orders = Order.objects.filter(user=self.request.user)
        service_statuses = ServiceStatus.objects.filter(user=self.request.user)
        print(orders)
        context['orders'] = orders
        context['service_statuses'] = service_statuses
        return context

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_superuser or not request.user.type == "tutor":
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


