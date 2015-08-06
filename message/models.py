#coding:UTF-8

import time
from django.db import models


class AppModel(models.Model):
    appName = models.CharField(max_length=50)
    appKey = models.CharField(max_length=50)
    createTime = models.DateTimeField()
    status = models.IntegerField(max_length=11)

    class Meta(object):
        db_table = "message_app"


class TokenModel(models.Model):
    appId = models.IntegerField(max_length=11)
    token = models.CharField(max_length=32)
    ableTime = models.DateTimeField()

    class Meta(object):
        db_table = "message_token"
