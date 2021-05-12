from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Goods
from .serializers import GoodsSerializer

# Create your views here.
class ListView(APIView):
    ''' url: http://127.0.0.1:8000/goods '''
    def get(self, request):
        ''' 获取所有 items 数据 '''
        # 利用 rest_framework ModelSerializer 实现返回 json 数据
        # 无需手动定义每个字段，只需指明需要序列化的字段名
        goods = Goods.objects.all()
        goods_serialzer = GoodsSerializer(instance=goods, many=True) # 序列化设置 instance
        return Response(goods_serialzer.data)

    def post(self, request):
        ''' 新增一个 item 数据 '''
        goods_serialzer = GoodsSerializer(data=request.data) # 反序列化设置 data
        if goods_serialzer.is_valid(raise_exception=True):
            goods_serialzer.save() # 调用 ModelSerializer create 方法
            return Response(goods_serialzer.data, status=status.HTTP_201_CREATED)
        return Response(goods_serialzer.errors)


class DetailView(APIView):
    ''' url: http://127.0.0.1:8000/goods/2 '''
    def get(self, request, index):
        ''' 获取一个 item 数据 '''
        try:
            goods = Goods.objects.get(id=index)
        except Goods.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        goods_serialzer = GoodsSerializer(instance=goods)
        return Response(goods_serialzer.data)

    def put(self, request, index):
        ''' 修改一个 item 数据 '''
        try:
            goods = Goods.objects.get(id=index)
        except Goods.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        goods_serialzer = GoodsSerializer(instance=goods, data=request.data, partial=True)
        if goods_serialzer.is_valid(raise_exception=True):
            goods_serialzer.save() # 调用 ModelSerializer update 方法
            return Response(goods_serialzer.data)
        return Response(goods_serialzer.errors)

    def delete(self, request, index):
        ''' 删除一个 item 数据 '''
        try:
            goods = Goods.objects.get(id=index)
        except Goods.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        goods.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
