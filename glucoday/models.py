# -*- coding: utf-8 -*-
import os, sys

from django.db import models
from django.contrib.auth.models import User



class BloodType(models.Model):
    description = models.CharField(max_length=120)



    def __unicode__(self):
        return self.description


class MeasurementContext(models.Model):
    description = models.CharField(max_length=120)


    def __unicode__(self):
        return self.description


class Glycemia(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    measurement = models.SmallIntegerField()
    measurement_context = models.ForeignKey(MeasurementContext)
    blood_type = models.ForeignKey(BloodType, )
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)



    def __unicode__(self):
        return self.measurement

    def get_absolute_url(self):
        return ('account_glycemia')

    def get_delete_url(self):
        return ('account_delete_glycemia', [self.id, ])