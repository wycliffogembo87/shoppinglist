# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import Shoppinglist, Shoppingitem


class ModelTestCase(TestCase):
    """This class defines the test suite for the shoppinglist and shoppingitem models."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="whitehat")
        self.shoppinglist_name = "Groceries"
        self.shoppinglist_budget = 500.00
        self.shoppingitem_name = "Mango"
        self.shoppinglist = Shoppinglist(
            name=self.shoppinglist_name, budget=self.shoppinglist_budget, owner=user)

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
        user = User.objects.create(username="whitehat")
    
        # Initialize client and force it to authenticate
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.shoppinglist_data = {'name': 'Groceries', 'budget': 500.00, 'owner': user.id}
        self.shoppingitem_data = {'name': 'Mangoes'}

    def test_api_can_create_shoppinglist(self):
        """Test the api has shoppinglist creation capability."""
        response = self.client.post(
            reverse('shoppinglists'), self.shoppinglist_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_create_shoppingitem(self):
        """Test the api has shoppingitem creation capability."""
        response = self.client.post(
            reverse('shoppingitems', args=[1]), self.shoppingitem_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_api_can_fetch_shoppinglists(self):
        """Test the api has shoppinglists fetching capability."""
        response = self.client.get(
            reverse('shoppinglists'), args=[1], format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_fetch_shoppingitems(self):
        """Test the api has shoppingitems fetching capability."""
        response = self.client.get(
            reverse('shoppingitems', args=[1]), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        response = new_client.get('/shoppinglists/', format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_update_shoppinglist(self):
         """Test the api can update a given shoppinglist."""
         change_shoppinglist = {'name': 'Something new'}
         response = self.client.put(
             reverse('shoppinglistdetails', kwargs={'shoppinglist_id': 1}),
             change_shoppinglist, format='json'
         )
         self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_shoppingitem(self):
         """Test the api can update a given shoppinglist item."""
         change_shoppinglist = {'name': 'new item name'}
         response = self.client.put(
             reverse('shoppinglistdetails', args=[1, 1]),
             change_shoppinglist, format='json'
         )
         self.assertEqual(response.status_code, status.HTTP_200_OK)
