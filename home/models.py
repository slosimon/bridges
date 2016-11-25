# -*- coding: utf-8 -*-
from django.db import models
from datetime import date, datetime
# Create your models here.

class Novica(models.Model):
	pub_date=models.DateTimeField()
	ime=models.TextField(max_length=500)
	novica=models.TextField(max_length=25500)
	def __unicode__(self):
		return self.ime

class Grafi(models.Model):
	graf=models.ImageField()
	opis=models.TextField(max_length=10000)
	po_vrsti=models.IntegerField()
	def __unicode__(self):
		return unicode(self.po_vrsti)
