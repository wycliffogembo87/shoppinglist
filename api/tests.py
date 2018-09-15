# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

from .models import Shoppinglist


class ModelTestCase(TestCase):
    """This class defines the test suite for the shoppinglist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.shoppinglist_name = "Groceries"
        self.shoppinglist_budget = 500.00
        self.shoppinglist = Shoppinglist(name=self.shoppinglist_name, budget=self.shoppinglist_budget)

    def test_model_can_create_a_shoppinglist(self):
        """Test the shoppinglist model can create a shoppinglist."""
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
        self.response = self.client.post(
            reverse('create'), self.shoppinglist_data, format="json"
        )

    def test_api_can_create_a_shopping_list(self):
        """Test the api has shoppinglist creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

