# -*- coding: utf-8 -*-
import os, sys

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class FoodType(models.Model):
    description = models.CharField(max_length = 160)

    def __unicode__(self):
        return self.description
    

class ExerciseRoutines(models.Model):
    user = models.ForeignKey(User,null=True,blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField("Descripción",max_length=150,null=True,blank=True)
    duration = models.SmallIntegerField("Duración",null=True,blank=True)
    distance = models.SmallIntegerField(null=True,blank=True)
    steps_number = models.SmallIntegerField("Número de pasos",null=True,blank=True)
    calories_burned = models.SmallIntegerField("Calorías quemadas",null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)

		
    def __unicode__(self):
		return self.name
	
    
    def get_absolute_url(self):
		return('list_patient')
	
    
    def get_delete_url(self):
                return ('delete_patient', [self.id, ])
            

class FoodRoutines(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    food_type = models.ForeignKey(FoodType,)
    portion_size = models.SmallIntegerField()
    amount_portion = models.SmallIntegerField()
    calories = models.SmallIntegerField()
    date_init = models.DateField()
    date_final = models.DateField()
    note = models.TextField(null=True, blank=True)

		
    def __unicode__(self):
		return self.name
	
    
    def get_absolute_url(self):
		return('list')
	
    
    def get_delete_url(self):
                return ('delete', [self.id, ])
