from functools import wraps

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

#
# def methods(str='POST'):
#     def methods_decorator(view_func):
#         @wraps(view_func)
#         def wrapped_view(*args, **kwargs):
#             return view_func(*args, **kwargs)
#         return wrapped_view
#     return methods_decorator




@csrf_exempt
def api_text(request):
    # 判断请求头是否为json
    if request.content_type != 'application/json':
        print(request.content_type)
        return HttpResponse(request.content_type,
                            status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    # 判断POST
    if request.method == 'POST':
        try:
            # 将请求json解析
            data = JSONParser().parse(request)
            # request.POST.get('mm', '')
        except Exception as e:
            print(e.args)
        else:
            content = dict(msg='SUCCESS')
            print(data)
            return JsonResponse(data=content, status=status.HTTP_200_OK)
    # 如果不是POST， 请求返回不支持的请求方法
    return HttpResponseNotAllowed(permitted_methods=['POST'])
