# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class NewsPaper(models.Model):
	nume = models.CharField(max_length=40)
	totalVanzari = models.IntegerField()
	hasCD = models.BooleanField(default=False, blank=True)
	hasBook = models.BooleanField(default=False, blank=True)
	priceWithoutAddons = models.IntegerField()
	priceWithCD = models.IntegerField(default=0, blank=True, null=True)
	priceWithBook =  models.IntegerField(default=0, blank=True, null=True)
	priceWithCDAndBook = models.IntegerField(default=0, blank=True, null=True)

	def publish(self):
		self.save()

	def __str__(self):
		return self.nume
