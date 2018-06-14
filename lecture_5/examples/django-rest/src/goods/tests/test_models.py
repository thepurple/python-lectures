"""
Test goods models
"""
from django.test import TransactionTestCase
from .factories import GoodsFactory


# Create your tests here.
class CompanyModelTest(TransactionTestCase):
    """
    Company View Unit testing for module Companies
    """

    @staticmethod
    def test_delete_goods():
        """
        Test that a company with a root division can be deleted
        :return:
        """
        goods = GoodsFactory()
        goods.delete()
