from django.urls import path
from accounts.views.accounts import AccountCreateView, logout_view, LoginView,PasswordChangeView, UserUpdateView, UserWithoutEmailUpdateView
from accounts.views.add_child import AddChildView

urlpatterns = [
    path('register/account/<str:type>/', AccountCreateView.as_view(), name='account_register'),
    path('account/<int:pk>/change-password/', PasswordChangeView.as_view(), name='change_password'),
    path('logout/', logout_view, name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/child/<int:pk>/', AddChildView.as_view(), name='add_child'),
    path('profile/<int:pk>/user_update', UserUpdateView.as_view(), name='user_update'),
    path('profile/<int:pk>/user_update_without_email', UserWithoutEmailUpdateView.as_view(), name='user_update_without_email'),

]
