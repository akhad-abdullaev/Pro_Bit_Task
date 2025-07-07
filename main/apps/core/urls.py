from django.urls import path
from . import views


urlpatterns = [
    path(
        "user-registration/",
        view=views.user_registration_api_view,
        name="user_registration"
    ),
    path(
        "user-login/",
        view=views.user_login_api_view,
        name="user_login"
    ),
    path(
        "<uuid:guid>/", 
        views.user_retrieve_delete_api_view, 
        name="user_detail"
    ),
    path(
        "<uuid:guid>/update/", 
        views.user_update_api_view, 
        name="user_update"
    ),
    path(
        "organization/create/", 
        views.organization_create_api_view,
        name="organization_create"
    )
]