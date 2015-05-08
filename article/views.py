from django.shortcuts import render_to_response, render
from article.models import Article, Offert
from forms import ArticleForm, OffertForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from random import randint
from datetime import date



# Create your views here.

@login_required
def articles(request):

	args = {}
	args.update(csrf(request))
	
	use=request.user.profile
	wanted_items = list()
	for e in Article.objects.all():
		if date.today()>e.q_date:
			e.state = 0
			e.save()
	
		kat=e.kategori
		if e.state==1 and getattr(use,kat):
			wanted_items.append(e)
	args['articles'] = wanted_items
	return render_to_response('articles.html', args)
	

@login_required
def article(request, article_id=1):
		e = Article.objects.get(id=article_id)
		if date.today()>e.q_date:
			e.state = 0
			e.save()
		return render(request, 'article.html', 
                  {'article': e })

	
@login_required	
def create(request):
		if request.POST:
			form = ArticleForm(request.POST, request.FILES, request.user)
			if form.is_valid():
				new_article = form.save(commit=False)
				new_article.owner = request.user

				new_article.save()

				return HttpResponseRedirect('/articles/my')
		else:
			form = ArticleForm()
			
		args = {}
		args.update(csrf(request))
		
		args['form'] = form
		
		return render_to_response('create_article.html', args)
					  				  

@login_required	
def add_offert(request, article_id):
	a = Article.objects.get(id=article_id)
	if date.today()>a.q_date:
		a.state = 0
		a.save()
	if a.state==1:
    
		if request.method == "POST":
			form = OffertForm(request.POST)
			if form.is_valid():
				c = form.save(commit=False)
				c.owner = request.user
				c.article_owner = a
				if a.Lowprice == 0:
					a.int1 = randint(5,6) * 200
					a.int2 = randint(4,5) * 500
					a.int3 = randint(4,5) * 1000
					a.int4 = randint(4,5) * 2000
					a.int5 = randint(8,9) * 2000
					a.int6 = randint(5,6) * 5000
					a.int7 = randint(8,9) * 5000
					a.int8 = randint(12,13) * 5000
					a.int9 = randint(15,16) * 5000
					
				if c.price<a.Lowprice or a.Lowprice==0:
					a.Lowprice=c.price
					if a.Lowprice<a.int1:
						a.intervall='0-'+ str(a.int1)
					elif a.Lowprice<a.int2:
						a.intervall= str(a.int1) + '-'+ str(a.int2)
					elif a.Lowprice<a.int3:
						a.intervall= str(a.int2) + '-'+ str(a.int3)
					elif a.Lowprice<a.int4:
						a.intervall= str(a.int3) + '-'+ str(a.int4)
					elif a.Lowprice<a.int5:
						a.intervall= str(a.int4) + '-'+ str(a.int5)
					elif a.Lowprice<a.int6:
						a.intervall= str(a.int5) + '-'+ str(a.int6)
					elif a.Lowprice<a.int7:
						a.intervall= str(a.int6) + '-'+ str(a.int7)
					elif a.Lowprice<a.int8:
						a.intervall= str(a.int7) + '-'+ str(a.int8)
					elif a.Lowprice<a.int9:
						a.intervall= str(a.int8) + '-'+ str(a.int9)
					elif a.Lowprice<100000:
						a.intervall= str(a.int9) + '- 100000'
					else:
						a.intervall= '100000+'
				a.quotation_amount = a.quotation_amount + 1
				c.save()
				a.save()
                     
				return HttpResponseRedirect('/articles/get/%s' % article_id)
        
		else:
			form = OffertForm()

		args = {}
		args.update(csrf(request))
    
		args['article'] = a
		args['form'] = form
    
		return render_to_response('add_offert.html', args)	
	
@login_required
def offerter_owner(request):
	args = {}
	args.update(csrf(request))


	args['offerter'] = Offert.objects.filter(owner=request.user)
	
	return render_to_response('offerter_owner.html', args)
	
