import re
import time
import logging

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from backweb.models import User


class LoginStatusMiddleware(MiddlewareMixin):

    def process_request(self, request):

        user_id = request.session.get('user_id')
        if user_id:
            admin = User.objects.filter(pk=user_id).first()
            request.admin = admin
            # 可以访问所有的页面
            return None
        not_need_path = ['/backweb/login/','/myapp/', '/media/']
        path = request.path
        print(path)
        for not_path in not_need_path:
            # 匹配当前路径是否为不需要登录验证的路径
            if re.match(not_path, path) or path == '/':
                return None
        # 当前的请求url不在not_need_path中，则表示当前url需要登录才能访问
        return HttpResponseRedirect(reverse('backweb:login'))


log = logging.getLogger(__name__)
class LogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 绑定在request上的一个属性
        request.init_time = time.time()


    def process_response(self, request, response):
        #请求时间
        count_time = time.time() - request.init_time
        # 请求状态码
        code = response.status_code
        #请求地址
        path = request.path
        #请求方法
        method = request.method
        #响应内容
        try:
            content = response.content
        except:
            content = response.streaming_content
        log_str = '%s %s %s %s %s' % (count_time, code, path, method, content)

        log.info(log_str)

        return response