from django.shortcuts import render_to_response, render
from offert.models import Offert
from article.models import Article
from forms import OffertForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def offerter(request):

	args = {}
	args.update(csrf(request))

	args['offerter'] = Offert.objects.all()	
	return render_to_response('offerter.html', args)

@login_required
def offert(request, offert_id=1):
    return render(request, 'offert.html', 
                  {'offert': Offert.objects.get(id=offert_id) })

@login_required	
def create(request):
		if request.POST:
			form = OffertForm(request.POST, request.user)
			if form.is_valid():
				new_offert = form.save(commit=False)
				new_offert.owner = request.user
				new_offert.article_owner = Article.objects.get(id=article_id)
				new_offert.save()
				
				return HttpResponseRedirect('/offerter/all')
		else:
			form = OffertForm()
			
		args = {}
		args.update(csrf(request))
		
		args['form'] = form
		
		return render_to_response('create_offert.html', args)
