from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешает только администраторам редактировать объект,
    остальные могут только просматривать (GET).
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # GET, HEAD, OPTIONS разрешены всем
        return request.user.is_authenticated and request.user.role == 'admin'


class IsOwner(permissions.BasePermission):
    """
    Разрешает доступ только владельцу объекта.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
