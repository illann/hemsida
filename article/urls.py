from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
	url(r'^all/$', 'article.views.articles'),
	url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
	url(r'^create/$', 'article.views.create'),

	url(r'^add_offert/(?P<article_id>\d+)/$', 'article.views.add_offert'),
	url(r'^my_quotations/$', 'article.views.offerter_owner')
		
) 

