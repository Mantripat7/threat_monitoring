from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminUserGroup(BasePermission):
    """
    Allows access only to users in Admin group.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.user.groups.filter(name="Admin").exists()
        )


class IsAnalystOrAdminReadOnly(BasePermission):
    """
    Admin: full access
    Analyst: read-only access
    """
    def has_permission(self, request, view):  
        if not request.user.is_authenticated:
            return False

        if request.method in SAFE_METHODS:
            return request.user.groups.filter(name__in=["Admin", "Analyst"]).exists()

        return request.user.groups.filter(name="Admin").exists()
