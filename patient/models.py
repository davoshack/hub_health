# -*- coding: utf-8 -*-
import os, sys

from django.db import models
from django.contrib.auth.models import User



class ClinicalSummary(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)



    def __unicode__(self):
        return self.summary

   