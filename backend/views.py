
from functools import wraps

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
import json

from backend.models import Person
from backend.serializers import PersonSerialzer

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
        except Exception as e:
            print(e.args)
        else:
            content = dict(msg='SUCCESS')
            print(data)
            return JsonResponse(data=content, status=status.HTTP_200_OK)
    # 如果不是POST， 请求返回不支持的请求方法
    return HttpResponseNotAllowed(permitted_methods=['POST'])


@csrf_exempt
def person_list(request):
    """
    list all code person, or create a new person
    :param request:
    :return:
    """
    if request.method == 'GET':
        person = Person.objects.all()[:8]
        serializer = PersonSerialzer(person, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # received_json_data = json.loads(request.body)
        # print(received_json_data)

        data = JSONParser().parse(request)
        serializer = PersonSerialzer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        # return HttpResponse(status=404)


@csrf_exempt
def person_detail(request, pk):
    """
    Retrieve, update or delete a code person
    :param request:
    :param pk:
    :return:
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PersonSerialzer(person)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonSerialzer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
