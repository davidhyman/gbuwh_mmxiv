from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from core import urls as core_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gbuwh.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^core/', include(core_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
