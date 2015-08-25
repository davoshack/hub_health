# -*- coding: utf-8 -*-
import os, sys

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now





class Country(models.Model):
    name = models.CharField(u"País", max_length=140)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=140)

    def __unicode__(self):
        return self.name


class MedicalEspecialty(models.Model):
    name = models.CharField(max_length=140)

    class Meta:
        verbose_name = u"Especialidad Médica"
        verbose_name_plural = u"Especialidad Médica"

    def __unicode__(self):
        return self.name


class ProfileUser(models.Model):
    user = models.OneToOneField(User)
    medical_specialty = models.ForeignKey(MedicalEspecialty, null=True, blank=True)
    medical_emphasis = models.CharField(max_length=255, null=True, blank=True)
    professional_abstract = models.TextField(null=True, blank=True)
    patient_abstract = models.TextField(null=True, blank=True)
    blood_group = models.CharField(max_length=4, null=True, blank=True,)
    sex = models.CharField(max_length=20)
    nationality = models.CharField(max_length=60, null=True, blank=True)
    date_birth = models.DateField(default=now, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    image = models.ImageField("Foto", upload_to='img/profile',
                              default='img/profile/avatar-default-user.png', null=True, blank=True)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)
    professional_register = models.CharField(max_length=300, null=True, blank=True)
    medical_consultation = models.BooleanField(default=False)
    flag_blood = models.BooleanField(default=False)
    flag_date_birth = models.BooleanField(default=False)
    flag_patient_abstract = models.BooleanField(default=False)
    flag_nationality = models.BooleanField(default=False)
    flag_message = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s, %s' % (self.user.last_name, self.user.first_name)

    class Meta:
        verbose_name = "Profile User"
        verbose_name_plural = "Profile User"

    def get_absolute_url(self):
        return self.image


User.profile_user = property(lambda u: ProfileUser.objects.get_or_create(user=u)[0])
