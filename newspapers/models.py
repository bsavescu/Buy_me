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
	stock = models.IntegerField(default=0)
	buyWithCD = False;
	buyWithBook = False;

	def publish(self):
		self.save()

	def calculatePrice(self):
		self.price = 0;
		if(self.buyWithCD):
			if(self.buyWithBook):
				self.price = self.priceWithCDAndBook
			else:
				self.price = self.priceWithCD
		else:
			if(self.buyWithBook):
				self.price = self.priceWithBook
			else:
				self.price = self.priceWithoutAddons
		return self.price


	def __str__(self):
		return self.nume

class CartObject:
	def __init__(self, newspaper, price, CD, Book):
		self.newspaper = newspaper
		self.price = price
		self.CD = CD
		self.Book = Book

	def __str__(self):
		to_print = self.newspaper.nume
		if self.CD :
			to_print += '+CD'
		if self.Book :
			to_print += '+Book'
		return to_print  