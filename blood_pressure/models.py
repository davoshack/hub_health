# -*- coding: utf-8 -*-
import os, sys

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class HeartBeat(models.Model):
    description = models.CharField(max_length = 120)
    
    class Meta:
		verbose_name = 'Latido'
		verbose_name_plural = 'Latido'
    
    def __unicode__(self):
        return self.description
 
   
class Pressure(models.Model):
    user = models.ForeignKey(User)
    systolic = models.SmallIntegerField(u"Sistólica (número superior)")
    diastolic = models.SmallIntegerField(u"Diastólica (número inferior)")
    bpm = models.SmallIntegerField("Pulso (latidos por minuto)");
    beat_status = models.ForeignKey(HeartBeat)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
    
    class Meta:
		verbose_name = 'Presion Arterial'
		verbose_name_plural = 'Presion Arterial'
		
    def __unicode__(self):
		return self.sistolica
	

    def get_absolute_url(self):
		return('account_blood_pressure')
	
  
    def get_delete_url(self):
                return ('account_delete_blood_pressure', [self.id, ])
