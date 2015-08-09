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


class DataModel(models.Model):
    "推送信息类"
    appId = models.IntegerField(max_length=11)
    title = models.CharField(max_length=50)
    message = models.TextField()
    messageType = models.IntegerField()
    createTime = models.DateTimeField()
    getTime = models.DateTimeField()

    class Meta:
        db_table = "message_data"


class AccountModel(models.Model):
    "后台管理员账号模型"
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=32)

    class Meta:
        db_table = "message_account"
