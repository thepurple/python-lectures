"""
Factories for goods module
"""
import factory
from factory import DjangoModelFactory


# pylint: disable=too-few-public-methods
# pylint: disable=unnecessary-lambda
class GoodsFactory(DjangoModelFactory):
    """
    Company factory
    """

    class Meta:
        model = 'goods.Goods'

    name = factory.Sequence(lambda n: 'Company name %d' % n)
    description = factory.Sequence(lambda n: 'Description %d' % n)
