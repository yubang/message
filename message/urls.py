from django.conf.urls import patterns, include, url
#from django.contrib import admin
from admin.urls import urlpatterns as adminUrlPatterns

urlpatterns = patterns('',
    url(r'^admin/',include(adminUrlPatterns)),
    #url(r'^admin/', include(admin.site.urls)),
)
