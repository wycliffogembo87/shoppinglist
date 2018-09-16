from rest_framework import serializers

from .models import Shoppinglist, Shoppingitem


class ShoppingitemSerializer(serializers.ModelSerializer):
    """Serializer to map the shoppingitem model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Shoppingitem
        fields = ('id', 'name')
        read_only_fields = ('date_created', 'date_modified')

class ShoppinglistSerializer(serializers.ModelSerializer):
    """Serializer to map the shoppinglist model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')
    shoppingitems = ShoppingitemSerializer(many=True, read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Shoppinglist
        fields = ('id', 'name', 'budget', 'owner', 'shoppingitems')
        read_only_fields = ('date_created', 'date_modified')

    def create(self, validated_data):
        return Shoppinglist.objects.create(**validated_data)
