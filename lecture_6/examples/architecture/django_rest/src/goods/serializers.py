"""
Goods module serializer
"""
from rest_framework import serializers
from .models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    """
    Goods serializer
    """

    class Meta:
        model = Goods
        fields = (
            'id', 'name', 'description', )
