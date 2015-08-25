# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Contacts(models.Model):
    from_user = models.ForeignKey(User)
    to_user = models.IntegerField()
    state = models.CharField(max_length=100, default="Pendiente")
    created = models.DateTimeField(auto_now_add=True)
    state_share_journal = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Contactos'
        verbose_name_plural = 'Contactos'

    def __unicode__(self):
        return self.from_user
