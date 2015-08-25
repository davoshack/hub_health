# -*- coding: utf-8 -*-
import os, sys

from django.db import models
from django.contrib.auth.models import User


class Hemoglobin(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    percent = models.DecimalField(max_digits=10, decimal_places=2);
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)

		
    def __unicode__(self):
		return self.percent
	
    
    def get_absolute_url(self):
		return('account_hemoglobin')
	
   
    def get_delete_url(self):
                return ('account_delete_hemoglobin', [self.id, ])
