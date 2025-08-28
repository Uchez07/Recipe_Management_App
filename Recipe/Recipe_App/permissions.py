# recipe_app/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only owners can edit or delete their recipes.
    Others have read-only access.
    """
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS → read-only
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only the recipe owner can modify it
        return obj.user == request.user
