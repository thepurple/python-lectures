"""
Tests for Goods module views
"""
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.status import (
    HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT)

from .factories import GoodsFactory
from ..models import Goods


class GoodsViewTest(APITestCase):
    """
    Test API endpoint with CRUD operations for Goods model.
    """

    def setUp(self):
        self.list_url = reverse('goods-list')

    def test_create(self):
        """
        Test .post() method
        """
        resp = self.client.post(self.list_url, {'name': 'test'})

        goods = Goods.objects.get()

        self.assertEqual(resp.status_code, HTTP_201_CREATED)
        self.assertEqual(resp.data,
                         {'id': goods.id,
                          'name': goods.name,
                          'description': goods.description})

    def test_get_list(self):
        """
        Test .get() method to retrieve a list
        """
        goods = GoodsFactory()
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, HTTP_200_OK)
        resp_data = {'id': goods.id,
                     'name': goods.name,
                     'description': goods.description}
        self.assertEqual(dict(resp.data[0]), resp_data)

    def test_get_item(self):
        """
        Test .get() method to retrieve an item
        """
        goods = GoodsFactory()

        url = reverse('goods-detail', args=[goods.id])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, HTTP_200_OK)

        resp_data = {'id': goods.id,
                     'name': goods.name,
                     'description': goods.description}
        self.assertEqual(resp.data, resp_data)

    def test_update(self):
        """
        Test .put() method
        """
        goods = GoodsFactory()

        new_name = 'new name'
        url = reverse('goods-detail', args=[goods.id])
        resp = self.client.put(url, {'name': new_name})

        self.assertEqual(resp.status_code, HTTP_200_OK)

        resp_data = {'id': goods.id,
                     'name': new_name,
                     "description": goods.description}
        self.assertEqual(resp.data, resp_data)

    def test_delete(self):
        """
        Test .delete() method
        """
        goods = GoodsFactory()

        url = reverse('goods-detail', args=[goods.id])
        resp = self.client.delete(url)

        self.assertEqual(resp.status_code, HTTP_204_NO_CONTENT)
        self.assertEqual(resp.data, None)
