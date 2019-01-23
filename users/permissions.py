from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsSelf(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user



