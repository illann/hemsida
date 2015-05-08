from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),
	(r'^articles/', include('article.urls')),
	(r'^accounts/', include('userprofile.urls')),
	url(r'^contact/$',  'hemsida.views.contact'),
	
	#url(r'auth/', include('django.contrib.auth.urls')),
	    
	
	# user auth urls
	url(r'^accounts/login/$',  'hemsida.views.login'),
	url(r'^accounts/auth/$',  'hemsida.views.auth_view'),    
	url(r'^accounts/logout/$', 'hemsida.views.logout'),
	url(r'^accounts/profile/$', 'hemsida.views.profile', name="profile"),
	url(r'^accounts/invalid/$', 'hemsida.views.invalid_login'),
	url(r'^accounts/password_change/$', 'hemsida.views.password_change', name="password_change"),
	url(r'^accounts/password_change_done/$', 'hemsida.views.password_change_done', name="password_change_done"),
	
)
