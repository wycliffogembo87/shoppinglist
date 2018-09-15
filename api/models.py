# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Shoppinglist(models.Model):
    """This class represents the Shoppinglist model."""
    
    name = models.CharField(max_length=255, blank=False, unique=True)
    budget = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""

        return {}.format(self.name)

class ShoppingItem(models.Model):
    """This class represents the ShoppingItem model."""
    
    shoppinglist = models.ForeignKey(Shoppinglist, related_name="shoppingitems")
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""

        return {}.format(self.name)
