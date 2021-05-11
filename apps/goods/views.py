import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
from .models import Goods

# Create your views here.
class GoodsListView(View):
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
        goods = Goods.objects.all()
        json_data = serializers.serialize('json', goods)
        return JsonResponse(json.loads(json_data), safe=False)
