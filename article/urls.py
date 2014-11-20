from django.conf.urls import patterns, include, url
# api import ArticleResource
#article_resource = ArticleResource()

urlpatterns = patterns('',
	url(r'^all/$', 'article.views.articles'),
	url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
	url(r'^create/$', 'article.views.create'),
	url(r'^delete_article/(?P<article_id>\d+)$', 'article.views.delete_article')
	
	
	#url(r'^like/(?P<article_id>\d+)/$', 'article.views.like_article'),
	#url(r'^search/$', 'article.views.search_titles'),
	#url(r'^api/', include(article_resource.urls)),
	
)
