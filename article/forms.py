from django import forms
from models import Article, Offert
from django.forms.fields import DateField
from article.models import Article
#from functools import partial

#DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class ArticleForm(forms.ModelForm):

	#del_date = forms.DateField(widget=DateInput())

	class Meta:
		model = Article
		fields = ('title', 'body', 'del_date', 'kvalitetskrav', 'material')
		widgets = {
			'del_date': forms.DateInput(attrs={'class':'datepicker'}),
		}
		
class DeleteNewForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = []

class OffertForm(forms.ModelForm):

	class Meta:
		model = Offert
		fields = ('body', 'price')

