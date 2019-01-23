from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, Relationship
from .serializers import UserSerializer, RelationshipSerializer
from .permissions import IsSelf

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.action == 'follow':
            return RelationshipSerializer

        return serializer

    def get_permissions(self):
        permissions = super().get_permissions()

        if self.action == 'create':
            return []

        if self.action == 'destroye':
            permissions.append(IsAdminUser())

        if self.action in ['update', 'partial_update']:
            permissions.append(IsSelf())

        return permissions

    @action(['POST'], True)
    def follow(self, request, pk):
        to_user = self.get_object()
        from_user = request.user

        relationship = Relationship.objects.create(
            to_user=to_user,
            from_user=from_user,
            is_agree=to_user.is_public,
        )

        return Response({'status':'ok'})
