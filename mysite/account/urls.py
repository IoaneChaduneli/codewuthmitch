from django.urls import path, include
from account.views import (registration_view, 
                            logout_view, 
                            login_view,
                            account_view,
                            must_authenticate_view,
                            )
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('register/', registration_view, name='user-register'),
    path('logout/', logout_view, name = 'user-logout'),
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),
    path('authenticate/',must_authenticate_view, name="must_authenticate"),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),



]
