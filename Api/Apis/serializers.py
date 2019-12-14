from rest_framework.serializers import ModelSerializer,DateTimeField
from .models import Goods

class GoodsSerializer(ModelSerializer):
    time = DateTimeField(format="%Y-%m-%d %H:%M:%S",required=False)
    class Meta:
        model = Goods
        fields = ['name','time']
