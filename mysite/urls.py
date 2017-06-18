from django.conf.urls import patterns, include, url
from mysite.views import test,first,second,category,lab


#from django.contrib import admin
#admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),


	(r'^test/$',test),
	(r'^first/$',first),
	(r'^second/$',second),
	(r'^lab/$',lab),
	(r'^category/$',category),
)
