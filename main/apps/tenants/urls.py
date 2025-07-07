from django.urls import path
from . import views


urlpatterns = [
    path(
        'api/auth/register/', 
        views.tenant_registration_api_view, 
        name='tenant_user_register'
    ),
    path(
        'api/auth/login/', 
        views.tenant_login_api_view, 
        name='tenant_user_register'
    ),
    path(
        'api/users/<int:pk>/me', 
        views.tenant_user_me_api_view, 
        name='tenant_user_login'
    ),
]
