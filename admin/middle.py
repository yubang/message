# coding:UTF-8

"""
后台管理中间件
"""

import re
from django.http import HttpResponseRedirect


class LoginCheck(object):
    "检查用户是否登录"

    def process_request(self, request):
        if re.search(r'^/admin/', request.path) and not re.search(r'^/admin/account', request.path):
            if 'admin' not in request.session:
                return HttpResponseRedirect("/admin/account")
        if re.search(r'^/admin/account', request.path):
            if 'admin' in request.session:
                return HttpResponseRedirect("/admin/")