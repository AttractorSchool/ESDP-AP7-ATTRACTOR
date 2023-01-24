from django.urls import path
from accounts.views.accounts import AccountCreateView, logout_view, LoginView, PasswordChangeView, UserUpdateView, \
    UserWithoutEmailUpdateView
from accounts.views.add_child import AddChildView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

urlpatterns = [
    path('register/account/<str:type>/', AccountCreateView.as_view(), name='account_register'),
    path('account/<int:pk>/change-password/', PasswordChangeView.as_view(), name='change_password'),
    path('logout/', logout_view, name='logout'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('register/child/<int:pk>/', AddChildView.as_view(), name='add_child'),
    path('profile/<int:pk>/user_update', UserUpdateView.as_view(), name='user_update'),
    path('profile/<int:pk>/user_update_without_email', UserWithoutEmailUpdateView.as_view(),
         name='user_update_without_email'),

    path('accounts/password_reset/', PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),

    path('reset-password/done', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),

    path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/',
         PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset-password/complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

]
