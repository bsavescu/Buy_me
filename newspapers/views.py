# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import NewsPaper
# from .forms import NewsPaperForm
# Create your views here.
def newspapers_list(request):
	# form_class = NewsPaperForm
    # if request is not post, initialize an empty form
	# form = form_class(request.POST or None)
	# if(request.method == 'POST'):
		
	# form = NewsPaperForm()
	print (request)
	newspapers = NewsPaper.objects.order_by('-totalVanzari')
	return render(request, 'newspapers/newspapers_list.html', {'newspapers' : newspapers})