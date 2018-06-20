"""
Goods views
"""
from django.http import Http404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Goods
from .serializers import GoodsSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    """
    API: Goods
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     """Retrieve a model instance."""
    #     return Response("Get")
    #
    # def list(self, request, *args, **kwargs):
    #     """List a queryset."""
    #     return Response("List")

    @staticmethod
    @action(methods=['get'], detail=True)
    def name(request, pk=None):     # pylint: disable=invalid-name
        """
        Get goods name by id

        :param request: request
        :param pk: goods id
        :return: response
        """
        try:
            goods = Goods.objects.filter(pk=pk)
            if goods:
                goods = goods.values('name')
            else:
                raise Http404
        except Exception as e:  # pylint: disable=invalid-name, unused-variable
            raise Http404
        return Response(goods)

    @staticmethod
    @action(methods=['get'], detail=False)
    def sorted(request, **kwargs):    # pylint: disable=invalid-name
        """
        Get goods list sorted by name

        :param request: request
        :param kwargs: kwargs (not required)
        :return: response with a goods list
        """
        queryset = Goods.objects.all().order_by("name")
        serializer = GoodsSerializer(
            queryset,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
