# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

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
