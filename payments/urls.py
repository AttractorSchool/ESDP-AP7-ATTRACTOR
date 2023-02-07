from django.urls import path

from payments.views import SelectServiceView, ServiceDetailView, OrderOnServiceCreateView, OrdersListView, OrderStatusUpdateView

urlpatterns = [
    path('services/', SelectServiceView.as_view(), name='service_select'),
    path('services/<int:pk>', ServiceDetailView.as_view(), name='service_detail'),
    path('create_order/<int:pk>/', OrderOnServiceCreateView.as_view(), name='order_on_service_create'),
    path('order_status_update/<int:pk>/', OrderStatusUpdateView.as_view(), name='order_status_update'),
    path('orders_list/', OrdersListView.as_view(), name='orders_list'),
]
