from django.db import models

# Create your models here.
from django.db import models
from ..common.models import BaseModel, BaseMeta
from django.utils.translation import gettext_lazy as _ 
from .managers import UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin



class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    is_owner = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255, verbose_name=_("Last name"))
    username = models.CharField(max_length=255, unique=True, verbose_name=_("Username"))
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admi site.",
        )
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting account"
            ),
    )
    is_superuser = models.BooleanField(_("superuser status"), default=False)
    objects = UserManager()

    USERNAME_FIELD = "username"

    class Meta(BaseMeta):
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f"{self.username}"
    
    @classmethod
    def validate_username(cls, username):
        if username:
            if User.objects.filter(username=username).exists():
                raise CustomValidationError("User already exists!")
            else:
                raise CustomValidationError("username required")
            


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    db_name = models.CharField(max_length=255, unique=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta(BaseMeta):
        verbose_name = _('organization')
        verbose_name_plural = _('organizations')

    def __str__(self):
        return f"{self.db_name}"