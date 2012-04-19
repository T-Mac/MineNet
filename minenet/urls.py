from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^login/$', 'Net.auth.login'),
	url(r'^addserver/$', 'Net.auth.addserver'),
	url(r'^validate/$', 'Net.auth.validate'),
    # Examples:
    # url(r'^$', 'minenet.views.home', name='home'),
    # url(r'^minenet/', include('minenet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
