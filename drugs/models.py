# -*- coding: utf-8 -*-
import os, sys

from django.db import models
from django.contrib.auth.models import User



class ConcentrationType(models.Model):
    description = models.CharField(max_length = 120)

    def __unicode__(self):
        return self.description
    

class DocisType(models.Model):
    description = models.CharField(max_length = 120)

    
    def __unicode__(self):
        return self.description

   
class AdministrationMode(models.Model):
    description = models.CharField(max_length = 120)

    def __unicode__(self):
        return self.description
    

class Drugs(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    concentration = models.SmallIntegerField(max_length=100)
    concentration_type = models.ForeignKey(ConcentrationType)
    docis = models.SmallIntegerField(max_length=100, blank=True, null=True)
    docis_type = models.ForeignKey(DocisType, blank=True, null=True)
    administration_mode = models.ForeignKey(AdministrationMode, blank=True, null=True)
    periodicity_administration = models.CharField(max_length=100)
    administration_cause = models.CharField(max_length=100, null=True, blank=True)
    date_init = models.DateField()
    date_final = models.DateField()
    note = models.TextField(null=True, blank=True)

    def __unicode__(self):
		return self.nombre
	
    
    def get_absolute_url(self):
		return('utilities_drugs')
	
    
    def get_delete_url(self):
                return ('utilities_delete_drugs', [self.id, ])
    


