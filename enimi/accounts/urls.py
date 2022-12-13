from django.urls import path

from accounts.views.accounts import AccountCreateView, logout_view, LoginView
from accounts.views.tutor_modules import TutorModuleCreateView

urlpatterns = [
    path('register/account/<str:type>/', AccountCreateView.as_view(), name='account_register'),
    path('logout/', logout_view, name='logout'),
    path('login/', LoginView.as_view(), name='login'),

    path('register/tutor/<int:pk>/', TutorModuleCreateView.as_view(), name='tutor_module_creation'),
]
