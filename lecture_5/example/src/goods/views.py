from rest_framework import viewsets
from .models import Goods
from .serializers import GoodsSerializer


# Create your views here.
class GoodsViewSet(viewsets.ModelViewSet):
    """
    API: Goods
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
