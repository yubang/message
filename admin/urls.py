#coding:UTF-8

from django.conf.urls import url ,patterns

urlpatterns = patterns('admin.views',
    url(r'^$', 'index'),
    url(r'^addApp$', 'addApp'),
    url(r'^deleteApp/(?P<app_id>\d+)$', 'deleteApp'),
    url(r'^detail/(?P<app_id>\d+)$', 'detail'),
    url(r'^addToken/(?P<app_id>\d+)$', 'addToken'),
    url(r'deleteToken/(?P<app_id>\d+)/(?P<token_id>\d+)$', 'deleteToken'),
)


