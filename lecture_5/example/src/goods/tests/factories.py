"""
Factories for goods module
"""
import factory
from factory import DjangoModelFactory


class GoodsFactory(DjangoModelFactory):
    """
    Company factory
    """
    # pylint: disable=unnecessary-lambda

    class Meta:
        model = 'goods.Goods'

    name = factory.Sequence(lambda n: 'Company name %d' % n)
    description = factory.Sequence(lambda n: 'Description %d' % n)
