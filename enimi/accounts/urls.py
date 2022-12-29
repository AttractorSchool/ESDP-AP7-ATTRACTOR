from django.urls import path

from accounts.views.accounts import AccountCreateView, logout_view, LoginView, PasswordChangeView
from accounts.views.add_child import AddChildView

urlpatterns = [
    path('register/account/<str:type>/', AccountCreateView.as_view(), name='account_register'),
    path('register/account/<int:pk>/change-password/', PasswordChangeView.as_view(), name='change_password'),
    path('logout/', logout_view, name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/child/<int:pk>/', AddChildView.as_view(), name='add_child')
]
