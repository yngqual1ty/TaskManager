from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Только владелец объекта или админ (is_staff) может получить доступ.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff

class IsAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff