# coding:UTF-8

import time
import json
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from message.models import TokenModel, AppModel, DataModel


def check_app_token_and_app_token(app_key, app_token):
    "检查appKey和appToken"
    try:
        obj = AppModel.objects.get(appKey=app_key)
    except ObjectDoesNotExist:
        return -1

    try:
        appToken = TokenModel.objects.get(appId=obj.id,token=app_token)
    except ObjectDoesNotExist:
        return -2

    if time.mktime(appToken.ableTime.timetuple()) - time.time() < 0 :
        return -3

    return obj.id


def get_push_message(request, app_key, app_token):
    "获取推送的信息"
    r = dict()
    r['messages'] = list()
    r['code'] = check_app_token_and_app_token(app_key, app_token)

    get_time = time.strftime("%Y-%m-%d %H:%M:%S")

    if r['code'] > 0:
        messages = DataModel.objects.order_by("-id").filter(appId=r['code'], getTime=None)
        update_obj = list()
        for obj in messages:
            obj_data = dict()
            obj_data['title'] = obj.title
            obj_data['message'] = obj.message
            obj_data['messageType'] = obj.messageType
            obj_data['createTime'] = obj.createTime.strftime("%Y-%m-%d %H:%M:%S")
            r['messages'].append(obj_data)
            update_obj.append(obj.id)
        if update_obj:
            DataModel.objects.filter(id__in=update_obj).update(getTime=get_time)
        r['code'] = 0

    response = HttpResponse(json.dumps(r))
    response['Content-Type'] = "application/json;charset=utf-8"
    return response


def push_message(request, app_key, app_token):
    "发送推送信息"

    if request.method != 'POST':
        return HttpResponseNotFound("你访问的网址不存在！")

    r = dict()
    r['messages'] = "发送信息出错！"
    r['code'] = check_app_token_and_app_token(app_key, app_token)

    if r['code'] > 0:
        title = request.POST.get('title', None)
        message = request.POST.get('message', None)
        message_type = request.POST.get('messageType', None)
        data = DataModel(appId=r['code'],title=title, message=message, messageType=message_type, createTime=time.strftime("%Y-%m-%d %H:%M:%S"))
        data.save()
        r['code'] = 0
        r['messages'] = "发送信息成功！"

    response = HttpResponse(json.dumps(r))
    response['Content-Type'] = "application/json;charset=utf-8"
    return response

