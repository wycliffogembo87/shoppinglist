# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

from .models import Shoppinglist, Shoppingitem


class ModelTestCase(TestCase):
    """This class defines the test suite for the shoppinglist and shoppingitem models."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.shoppinglist_name = "Groceries"
        self.shoppinglist_budget = 500.00
        self.shoppingitem_name = "Mango"
        self.shoppinglist = Shoppinglist(name=self.shoppinglist_name, budget=self.shoppinglist_budget)

    def test_model_can_create_a_shoppinglist(self):
        """Test the shoppingitem model can create a shoppingitem."""
        old_count = Shoppinglist.objects.count()
        self.shoppinglist.save()
        new_count = Shoppinglist.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """This class defines the test suite for the api view."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.shoppinglist_data = {'name': 'Groceries', 'budget': 500.00}
        self.shoppingitem_data = {'name': 'Mango'}
        self.response_create_shoppinglist = self.client.post(
            reverse('shoppinglists'), self.shoppinglist_data, format="json"
        )
        self.response_create_shoppingitem = self.client.post(
            reverse('shoppingitems', args=[1]), self.shoppinglist_data, format="json"
        )
        self.response_fetch_shoppinglists = self.client.get(
            reverse('shoppinglists'), format="json"
        )
        self.response_fetch_shoppingitems = self.client.get(
            reverse('shoppingitems', args=[1]), format="json"
        )

    def test_api_can_create_a_shoppinglist(self):
        """Test the api has shoppinglist creation capability."""
        self.assertEqual(self.response_create_shoppinglist.status_code, status.HTTP_201_CREATED)

    def test_api_can_create_a_shoppingitem(self):
        """Test the api has shoppingitem creation capability."""
        self.assertEqual(self.response_create_shoppingitem.status_code, status.HTTP_201_CREATED)

    def test_api_can_fetch_shoppinglists(self):
        """Test the api has shoppinglists fetching capability."""
        self.assertEqual(self.response_fetch_shoppinglists.status_code, status.HTTP_200_OK)

    def test_api_can_fetch_shoppingitems(self):
        """Test the api has shoppingitems fetching capability."""
        self.assertEqual(self.response_fetch_shoppingitems.status_code, status.HTTP_200_OK)
