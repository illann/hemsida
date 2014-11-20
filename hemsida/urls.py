from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hemsida.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	(r'^articles/', include('article.urls')),
	(r'^accounts/', include('userprofile.urls')),
	    
	
	# user auth urls
	url(r'^accounts/login/$',  'hemsida.views.login'),
	url(r'^accounts/auth/$',  'hemsida.views.auth_view'),    
	url(r'^accounts/logout/$', 'hemsida.views.logout'),
	url(r'^accounts/loggedin/$', 'hemsida.views.profile'),
	url(r'^accounts/invalid/$', 'hemsida.views.invalid_login'),
	
	
)
