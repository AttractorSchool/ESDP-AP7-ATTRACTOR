from django.urls import path

from accounts.views.accounts import AccountCreateView, logout_view, LoginView

urlpatterns = [
    path('register/account/<str:type>/', AccountCreateView.as_view(), name='account_register'),
    path('logout/', logout_view, name='logout'),
    path('login/', LoginView.as_view(), name='login')
]
