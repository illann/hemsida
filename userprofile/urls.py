from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
		url(r'^profile/$', 'userprofile.views.user_profile'),
		url(r'^category_selection/$', 'userprofile.views.category_selection'),
)