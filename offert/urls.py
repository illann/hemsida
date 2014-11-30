from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all/$', 'offert.views.offerter'),
	url(r'^get/(?P<offert_id>\d+)/$', 'offert.views.offert'),
	url(r'^create/$', 'offert.views.create'),
)