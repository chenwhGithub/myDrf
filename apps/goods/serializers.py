from rest_framework import serializers

class GoodsSerializer(serializers.Serializer):
    # 属性名必须与 model 定义的一致
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    image = serializers.ImageField()
