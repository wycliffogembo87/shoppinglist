# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics
from .serializers import ShoppinglistSerializer
from .serializers import ShoppingitemSerializer
from .models import Shoppinglist, Shoppingitem


class ShoppinglistAPIView(generics.ListCreateAPIView):
    """This class defines the shoppinglist create behaviour of our rest api."""
    queryset = Shoppinglist.objects.all()
    serializer_class = ShoppinglistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new shoppinglist."""
        serializer.save(user=self.request.user)

class ShoppingitemAPIView(generics.ListCreateAPIView):
    """This class defines the shoppingitem create behaviour of our rest api."""
    queryset = Shoppingitem.objects.all()
    serializer_class = ShoppingitemSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new shoppingitem."""
        serializer.save(shoppinglist_id=self.kwargs['pk'])
