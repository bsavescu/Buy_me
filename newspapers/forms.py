from django import forms
from .models import NewsPaper

class NewsPaperForm(forms.ModelForm):
	class Meta:
		model = NewsPaper
        fields = ['nume','totalVanzari']

    # def __init__(self, *args, **kwargs):          
    #     super(NewsPostForm, self).__init__(*args, **kwargs)