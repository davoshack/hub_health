# -*- coding: utf-8 -*-
import os, sys

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class AcademicProfile(models.Model):
    user = models.ForeignKey(User)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    achievements = models.TextField()
    date_init = models.DateField()
    date_final = models.DateField()
    current = models.BooleanField(default=False)



    def __unicode__(self):
        return self.institution


    def get_absolute_url(self):
        return ('specialist_academic')


class ProfessionalProfile(models.Model):
    user = models.ForeignKey(User)
    organization = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    function = models.TextField()
    date_init = models.DateField()
    date_final = models.DateField()
    location = models.CharField(max_length=255)
    current = models.BooleanField(default=False)




    def __unicode__(self):
        return self.organization

    def get_absolute_url(self):
        return ('specialist_professional')


class EmploymentHistory(models.Model):
    user = models.ForeignKey(User)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(max_length=25, null=True, blank=True)
    mobile = models.CharField(max_length=30, null=True, blank=True)
    institution = models.CharField(max_length=300)
    image = models.ImageField(upload_to='img/employment',
                              default='img/Fotolia_Subscription_Monthly_P.jpg', null=True, blank=True)


    def __unicode__(self):
        return self.institution

    def get_absolute_url(self):
        return ('specialist_edit_employmenthistory')