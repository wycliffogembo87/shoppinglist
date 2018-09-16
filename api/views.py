# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwner
from .serializers import ShoppinglistSerializer
from .serializers import ShoppingitemSerializer
from .models import Shoppinglist
from .models import Shoppingitem


class ShoppinglistListView(generics.ListCreateAPIView):
    """This class defines the shoppinglist create behaviour of our rest api."""
    serializer_class = ShoppinglistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new shoppinglist."""
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Shoppinglist.objects.all()
        shoppinglist = (self.kwargs).get('shoppinglist_id')

        if shoppinglist:
            queryset = queryset.filter(id=shoppinglist)

        return queryset

class ShoppingitemListView(generics.ListCreateAPIView):
    """This class defines the shoppinglist create behaviour of our rest api."""
    serializer_class = ShoppingitemSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new shoppinglist."""
        serializer.save(
            shoppinglist_id=self.kwargs['shoppinglist_id']
        )

    def get_queryset(self):
        queryset = Shoppingitem.objects.all()

        shoppinglist = (self.kwargs).get('shoppinglist_id')
        shoppingitem = (self.kwargs).get('shoppingitem_id')

        if shoppinglist and shoppingitem:
            queryset = queryset.filter(id=shoppingitem, shoppinglist_id=shoppinglist)
        elif shoppinglist:
            queryset = queryset.filter(shoppinglist_id=shoppinglist)

        return queryset
        

class ShoppinglistDetailView(generics.RetrieveUpdateDestroyAPIView):
    """This class defines the shoppinglist update behaviour of our rest api."""
    serializer_class = ShoppinglistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    lookup_url_kwarg = 'shoppinglist_id'

    def get_queryset(self):
        shoppinglist = self.kwargs['shoppinglist_id']
        return Shoppinglist.objects.filter(id=shoppinglist)
