from django import forms
from models import Article, Offert
from django.forms.fields import DateField
from article.models import Article


class ArticleForm(forms.ModelForm):



	class Meta:
		model = Article
		fields = ('title', 'body', 'del_date', 'filer')
		widgets = {
			'del_date': forms.DateInput(attrs={'class':'datepicker'}),
		}
		
class OffertForm(forms.ModelForm):

	class Meta:
		model = Offert
		fields = ('body', 'price')

