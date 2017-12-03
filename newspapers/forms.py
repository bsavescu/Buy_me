from django import forms
from .models import NewsPaper

class NewsPaperForm(forms.ModelForm):
	class Meta:
		model = NewsPaper
        fields = ['nume','totalVanzari']
