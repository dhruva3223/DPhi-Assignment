from rest_framework.permissions import BasePermission
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAuthorizedUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
class IsAuthorizedUserExceptPost(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )