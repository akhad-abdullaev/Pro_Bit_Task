from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models



class TenantUser(AbstractUser):
    full_name = models.CharField(max_length=255)

    groups = models.ManyToManyField(
        Group,
        related_name='tenantuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='tenantuser_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
