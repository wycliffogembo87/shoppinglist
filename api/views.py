# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics
from .serializers import ShoppinglistSerializer
from .models import Shoppinglist


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behaviour of our rest api."""
    queryset = Shoppinglist.objects.all()
    serializer_class = ShoppinglistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new shoppinglist."""
        serializer.save()
