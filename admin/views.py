# coding:UTF-8

import time
import hashlib
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from message.models import AppModel, TokenModel, AccountModel


def index(request):
    apps = AppModel.objects.order_by("-id").filter(status=0)
    return render_to_response("admin/index.html", {'apps': apps})


def addApp(request):
    app_name = request.POST.get("appName", None)
    app_key = hashlib.md5(str(time.time())).hexdigest()
    app_model = AppModel(appName=app_name, appKey=app_key, status=0, createTime=time.strftime("%Y-%m-%d %H:%M:%S"))
    app_model.save()
    return HttpResponseRedirect("/admin/")


def deleteApp(request, app_id):
    AppModel.objects.filter(id=app_id).update(status=2)
    return HttpResponseRedirect("/admin/")


def detail(request, app_id):
    "显示应用详情"
    app = AppModel.objects.get(id=app_id)
    appTokens = TokenModel.objects.filter(appId=app_id)
    return render_to_response("admin/detail.html", {"app": app, "appTokens": appTokens})


def addToken(request, app_id):
    "添加应用token"
    token = request.POST.get("token", None)
    able_time = request.POST.get("ableTime", None)
    obj = TokenModel(appId=app_id, token=token, ableTime=able_time)
    obj.save()
    return HttpResponseRedirect("/admin/detail/%s" % (app_id,))


def deleteToken(request, app_id, token_id):
    "删除应用token"
    TokenModel.objects.filter(id=token_id, appId=app_id).delete()
    return HttpResponseRedirect("/admin/detail/%s" % (app_id,))

def account(request):
    "账号登录"

    if request.method == "GET":
        error = request.GET.get("error", 0)
        return render_to_response("admin/account.html", {})
    else:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        try:
            account_model = AccountModel.objects.get(username=username)
        except ObjectDoesNotExist:
            return HttpResponseRedirect("/admin/account?error=1")

        if account_model.password == hashlib.md5(password).hexdigest():
            request.session['admin'] = time.time()
            return HttpResponseRedirect("/admin/")
        else:
            return HttpResponseRedirect("/admin/account?error=2")


def exit_account(request):
    "用户退出"
    if 'admin' in request.session:
        del request.session['admin']
    return HttpResponseRedirect("/admin/account")





