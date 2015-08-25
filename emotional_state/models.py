# -*- coding: utf-8 -*-
import os, sys

from django.db import models
from django.contrib.auth.models import User


class ListEmotionalStates(models.Model):
    description = models.CharField(max_length = 120)
    
    def __unicode__(self):
        return self.description
    

          
class EmotionalStatesPatient(models.Model):
    
    user = models.ForeignKey(User)
    state = models.SmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)

              

		
    def __unicode__(self):
		return self.state
	

    def get_absolute_url(self):
		return('account_emotionalstates')
	

    def get_delete_url(self):
                return ('account_emotionalstates', [self.id, ])
