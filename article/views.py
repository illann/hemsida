from django.shortcuts import render_to_response, render
from article.models import Article, Offert
from django.http import HttpResponse
from forms import ArticleForm, OffertForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
#from django.shortcuts import render, get_object_or_404

#from .forms import DeleteNewForm
from django.template import RequestContext
#from django.contrib import messages


# Create your views here.

@login_required
def articles(request):

	args = {}
	args.update(csrf(request))

	args['articles'] = Article.objects.all()	
	return render_to_response('articles.html', args)

@login_required
def article(request, article_id=1):
    return render(request, 'article.html', 
                  {'article': Article.objects.get(id=article_id) })

"""							 
def language(request, language='en-gb'):
	response = HttpResponse("setting language to %s" % language)
	
	response.set_cookie('lang', language)
	
	request.session['lang'] = language 
	
	return response
"""	
	
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
def delete_article(request, article_id):
    c = Article.objects.get(id=article_id).delete()
    #article_id = c.article.id
    #c.delete()
    
    return HttpResponseRedirect('/articles/all')


@login_required
def articles_owner(request):
	args = {}
	args.update(csrf(request))

	args['articles'] = Article.objects.filter(owner=request.user)
	# filter articles based on owner
	
	return render_to_response('articles_owner.html', args)
	
	
def add_offert(request, article_id):
    a = Article.objects.get(id=article_id)
    
    if request.method == "POST":
        f = OffertForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.owner = request.user
            c.article_owner = a
            c.save()
            
            
            return HttpResponseRedirect('/articles/get/%s' % article_id)
        
    else:
        f = OffertForm()

    args = {}
    args.update(csrf(request))
    
    args['article'] = a
    args['form'] = f
    
    return render_to_response('add_offert.html', args)	
	
	
"""
		
def delete_article(request, new_id):
    new_to_delete = get_object_or_404(Article, id=new_id)
    #+some code to check if this object belongs to the logged in user

    if request.method == 'POST':
        form = DeleteNewForm(request.POST, instance=new_to_delete)
        if form.is_valid(): # checks CSRF
            new_to_delete.delete()
			
            return HttpResponseRedirect("'/articles/all'") # wherever to go after deleting

    else:
        form = DeleteNewForm(instance=new_to_delete)

    template_vars = {'form': form}
    return render(request, 'delete_article.html', template_vars)		
		
"""

"""		
def	like_article(request, article_id):
	if article_id:
		a = Article.objects.get(id=article_id)
		count = a.likes
		count += 1
		a.likes = count
		a.save()
		
	return HttpResponseRedirect('/articles/get/%s' % article_id)

def search_titles(request):
    articles = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))            
    
    return render_to_response('ajax_search.html', {'articles' : articles})

"""
