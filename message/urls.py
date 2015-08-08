from django.conf.urls import patterns, include, url
#from django.contrib import admin
from admin.urls import urlpatterns as adminUrlPatterns
from api.urls import urlpatterns as api_url_patterns

urlpatterns = patterns('',
    url(r'^admin/', include(adminUrlPatterns)),
    url(r'^api/', include(api_url_patterns)),
)
