from django.db import models
from django.utils.translation import ugettext_lazy as _


class Banks(models.Model):
    id = models.BigIntegerField(_("Bank ID"), primary_key=True, unique=True,null=False)
    name = models.CharField(_("Bank Name"), max_length=50)

    class Meta:
        verbose_name = _("Bank")
        verbose_name_plural = _("Banks")

    def __str__(self):
        return self.name


class Branches(models.Model):
    ifsc = models.CharField(max_length=11, null=False)
    bank = models.ForeignKey(Bank, related_name="bank_branches")
    branch = models.CharField(_("Branch"), max_length=75)
    address = models.CharField(_("Address"), max_length=195)
    city = models.CharField(_("City"), max_length=50)
    district = models.CharField(_("District"), max_length=50)
    state = models.CharField(_("State"), max_length=26)

    class Meta:
        verbose_name = _("Branch")
        verbose_name_plural = _("Branches")

    def __str__(self):
        return self.ifsc + ": " + self.bank
