from django.conf.urls import patterns, include, url
# api import ArticleResource
#article_resource = ArticleResource()

urlpatterns = patterns('',
	url(r'^all/$', 'article.views.articles'),
	url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
	url(r'^create/$', 'article.views.create'),
	url(r'^delete_article/(?P<article_id>\d+)$', 'article.views.delete_article'),
	url(r'^my/$', 'article.views.articles_owner'),
	url(r'^inkomna_offerter/$', 'article.views.articles_inkomna_offerter'),
	#url(r'^add_comment/(?P<article_id>\d+)/$', 'article.views.add_comment')
	url(r'^add_offert/(?P<article_id>\d+)/$', 'article.views.add_offert'),
	url(r'^get_article_offert/(?P<article_id>\d+)/$', 'article.views.article_med_offert')
	
	
	#url(r'^like/(?P<article_id>\d+)/$', 'article.views.like_article'),
	#url(r'^search/$', 'article.views.search_titles'),
	#url(r'^api/', include(article_resource.urls)),
	
)
