from django.contrib import admin

from main.apps.core.models import Organization, User

admin.site.register(User)
admin.site.register(Organization)