from django import forms
from models import Offert



class OffertForm(forms.ModelForm):

	class Meta:
		model = Offert
		fields = ('body', 'price')
