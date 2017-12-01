from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.newspapers_list, name='newspapers_list'),
]