
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, Http404
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


from backend.models import Person
from backend.serializers import PersonSerialzer

#
# @csrf_exempt
# def api_text(request):
#     # 判断请求头是否为json
#     if request.content_type != 'application/json':
#         print(request.content_type)
#         return HttpResponse(request.content_type,
#                             status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
#     # 判断POST
#     if request.method == 'POST':
#         try:
#             # 将请求json解析
#             data = JSONParser().parse(request)
#             # request.POST.get('mm', '')
#         except Exception as e:
#             print(e.args)
#         else:
#             content = dict(msg='SUCCESS')
#             print(data)
#             return JsonResponse(data=content, status=status.HTTP_200_OK)
#     # 如果不是POST， 请求返回不支持的请求方法
#     return HttpResponseNotAllowed(permitted_methods=['POST'])


# # 1.0
# # @csrf_exempt
# @api_view(['GET', 'POST'])  # 该装饰器限定指示的方法， 默认只有GET方法， 其他请求会报405错误。
# def person_list(request, format=None):
#     if request.method == 'GET':
#         person = Person.objects.all()[:8]
#         serializer = PersonSerialzer(person, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         # 该对象 TemplateResponse采用未呈现的内容病使用内用协商来确定返回给客户端的正确内容类型
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         # data = JSONParser().parse(request)
#         serializer = PersonSerialzer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         # return HttpResponse(status=404)
#
#
# # @csrf_exempt
# @api_view(['GET', 'POST'])
# def person_detail(request, pk, format=None):
#     try:
#         person = Person.objects.get(pk=pk)
#     except Person.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = PersonSerialzer(person)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         # data = JSONParser().parse(request)
#         serializer = PersonSerialzer(person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# # 2.0 使用APIView
# class PersonList(APIView):
#     def get(self, request, format=None):
#         persons = Person.objects.all()
#         serializer = PersonSerialzer(persons, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = PersonSerialzer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PersonDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Person.objects.get(pk=pk)
#         except Person.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         person = self.get_object(pk)
#         serializer = PersonSerialzer(person)
#         return Response(serializer.data)
#
#     def post(self, request, pk, format=None):
#         person = self.get_object(pk)
#         serializer = PersonSerialzer(person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#


#
# """
# |______________mixins___________|_____http______|
# |   mixins.ListModelMixin       |      GET      |
# |   mixins.CreateModelMixin     |     POST      |
# |   mixins.RetrieveModelMixin   |      GET      |
# |   mixins.UpdateModelMixin     |   PUT/PATCH   |
# |   mixins.DestroyModelMixin    |     DELETE    |
# -------------------------------------------------
# """
# # 3.0 使用 mixins
# class PersonList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerialzer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class PersonDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerialzer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#


# 4.0 通用视图
class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerialzer


class PersonDetail(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerialzer
