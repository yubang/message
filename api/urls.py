# coding:UTF-8

from django.conf.urls import patterns,url

urlpatterns = patterns('api.views',
    url(r'^getPushMessage/(?P<app_key>\w+)/(?P<app_token>\w+)$', 'get_push_message'),
    url(r'^pushMessage/(?P<app_key>\w+)/(?P<app_token>\w+)$', 'push_message'),
)
