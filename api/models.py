# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Shoppinglist(models.Model):
    """This class represents the Shoppinglist model."""
    
    name = models.CharField(max_length=255, blank=False, unique=True)
    budget = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    owner = models.ForeignKey(
        'auth.User', related_name="shoppinglists", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""

        return {}.format(self.name)

class Shoppingitem(models.Model):
    """This class represents the ShoppingItem model."""
    
    name = models.CharField(max_length=255, blank=False, unique=True)
    shoppinglist = models.ForeignKey(
        Shoppinglist, related_name="shoppingitems", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""

        return {}.format(self.name)
