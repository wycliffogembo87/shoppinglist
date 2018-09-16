from rest_framework.permissions import BasePermission
from .models import Shoppinglist


class IsOwner(BasePermission):
    """Custom permission class to allow only shoppinglist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the shoppinglist owner."""
        if isinstance(obj, Shoppinglist):
            return obj.owner == request.user
        return obj.owner == request.user
