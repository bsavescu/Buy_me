# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import F
from django.shortcuts import render
from .models import NewsPaper, CartObject
# from .forms import NewsPaperForm
# Create your views here.

cart_list = []
filter_bar = ['All','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
def newspapers_list(request):
	# form_class = NewsPaperForm
    # if request is not post, initialize an empty form
	# form = form_class(request.POST or None)
	# if(request.method == 'POST'):
		
	# form = NewsPaperForm()
	totalPrice = 0
	newspapers = NewsPaper.objects.order_by('-totalVanzari') 
	if request.method == 'GET':
		if 'csrfmiddlewaretoken' in request.GET:
			if 'add_to_cart' in request.GET:
				newspaper_name = request.GET.getlist('add_to_cart')[0].split("_")[0]
				newspaper = NewsPaper.objects.get(nume=newspaper_name)
				if 'options' in request.GET:
					if len(request.GET.getlist('options')) == 2 :
						cart_obj = CartObject(newspaper, newspaper.priceWithCDAndBook, True, True)
					else:
						if request.GET.getlist('options')[0] == 'BuyWithCD' :
							cart_obj = CartObject(newspaper, newspaper.priceWithCD, True, False)
						else:
							cart_obj = CartObject(newspaper, newspaper.priceWithBook, False, True)
				else:
					cart_obj = CartObject(newspaper, newspaper.priceWithoutAddons, False, False)
				cart_list.append(cart_obj)
		if 'filter' in request.GET:
			filter_option = request.GET.getlist('filter')[0]
			if filter_option != 'All':
				newspapers = NewsPaper.objects.filter(nume__startswith = filter_option).order_by('-totalVanzari')
				print newspapers 
	
	if request.method == 'POST':
		if 'buy' in request.POST :
			for i in range(len(cart_list)):
				obj = cart_list.pop()
				NewsPaper.objects.all().select_related().filter(nume = obj.newspaper.nume).update(stock = F('stock')-1)
		if 'dismiss' in request.POST :
			for i in range(len(cart_list)):
				cart_list.pop()
		if 'delete' in request.POST:
			to_be_deleted = request.POST.getlist('delete')[0].split("_")
			print to_be_deleted
			for obj in cart_list:
				if obj.__str__() == to_be_deleted[0]:
					cart_list.remove(obj)
	
	for obj in cart_list:
		totalPrice += obj.price
	
	return render(request, 'newspapers/newspapers_list.html', {'newspapers' : newspapers, 'cart_list' : cart_list, 'filter_bar' : filter_bar, 'totalPrice' : totalPrice})