import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Goods
from .serializers import GoodsSerializer

# Create your views here.
class ListView(APIView):
    def get(self, request):
        # 利用 View 实现返回 json 数据：
        # json_list = []
        # goods = Goods.objects.all()
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['price'] = good.price
        #     json_list.append(json_dict)
        # return HttpResponse(json.dumps(json_list), content_type='application/json')


        # 利用 model_to_dict 实现返回 json 数据：
        # 不需要繁琐指定每个字段的生成，但是无法序列化 ImageFieldFile 和 DateTimeField
        # json_list = []
        # goods = Goods.objects.all()
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        # return HttpResponse(json.dumps(json_list), content_type='application/json')


        # 利用 django serializers 实现返回 json 数据：
        # 可以序列化 ImageFieldFile 和 DateTimeField，但是序列化后的格式不能修改
        # goods = Goods.objects.all()   
        # json_data = serializers.serialize('json', goods)
        # return JsonResponse(json.loads(json_data), safe=False)


        # 利用 rest_framework serializers 实现返回 json 数据：
        # 可以自动以序列化的字段，ImageFieldFile 字段返回全路径
        # goods = Goods.objects.all()
        # goods_serialzer = GoodsSerializer(goods, many=True)
        # return Response(goods_serialzer.data)


        # 利用 rest_framework ModelSerializer 实现返回 json 数据：
        # 无需手动定义每个字段，只需指明需要序列化的字段名
        goods = Goods.objects.all()
        goods_serialzer = GoodsSerializer(instance=goods, many=True)
        return Response(goods_serialzer.data)

    def post(self, request):
        """ 新增 """
        goods_serialzer = GoodsSerializer(data=request.data)
        if goods_serialzer.is_valid(raise_exception=True):
            goods_serialzer.save()
            return Response(goods_serialzer.data, status=status.HTTP_201_CREATED)
        return Response(goods_serialzer.errors)


class DetailView(APIView):
    def get(self, request, index):
        try:
            goods = Goods.objects.get(id=index)
        except Goods.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        goods_serialzer = GoodsSerializer(instance=goods)
        return Response(goods_serialzer.data)

    def put(self, request, index):
        try:
            goods = Goods.objects.get(id=index)
        except Goods.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        goods_serialzer = GoodsSerializer(instance=goods, data=request.data, partial=True)
        if goods_serialzer.is_valid(raise_exception=True):
            goods_serialzer.save()
            return Response(goods_serialzer.data)
        return Response(goods_serialzer.errors)

    def delete(self, request, index):
        try:
            goods = Goods.objects.get(id=index)
        except Goods.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        goods.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
