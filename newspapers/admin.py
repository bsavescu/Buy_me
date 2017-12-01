# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import NewsPaper
# Register your models here.

class NewsPaperAdminForm(admin.ModelAdmin):
    exclude = ('buyWithCD','buyWithBook')
admin.site.register(NewsPaper,NewsPaperAdminForm)