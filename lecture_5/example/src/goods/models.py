from django.db import models
from django.utils.translation import gettext_lazy as _


class Goods(models.Model):
    """
    Goods and services model
    """

    name = models.CharField(
        max_length=30, unique=True,
        help_text=_('Goods name'))
    description = models.CharField(
        max_length=255, unique=False,
        null=True, blank=True,
        help_text=_('Goods description'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Goods')
        verbose_name_plural = _("Goods")
