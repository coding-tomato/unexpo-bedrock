from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from userHome.models import UserHome

# Create your models here.

"""
    Extending the existing User model for storing information of registered users.
"""


class UserData(models.Model):
    """
    store information related to User,
    using a OneToOneField to a model
    containing the fields for additional information
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="usersdata",
    )

    # Field that allows choosing level of access
    class AccessLevel(models.TextChoices):
        ADMIN_LEVEL = 'AL', _('Administrador')
        NORMAL_LEVEL = 'NL', _('Normal')
        LIMITED_LEVEL = 'LL', _('Limitado')

    accessLevel = models.CharField(
        max_length=3,
        choices=AccessLevel.choices,
        default=AccessLevel.NORMAL_LEVEL,
        verbose_name="Nivel de acceso",
    )

    # Field that allows selecting if the user is blocked or not
    locks = models.BooleanField(
        default=False,
        verbose_name="Bloqueado"
    )

    # Foreign key for a relationship between the home model and user model
    home = models.ForeignKey(
        UserHome,
        related_name="usersdata",
        on_delete=models.CASCADE,
    )

    # Converts data to a string
    def __str__(self):
        return "Nivel= %s | Bloqueado= %s | Casa= %s" % (
            self.accessLevel,
            self.locks,
            self.home,
        )
