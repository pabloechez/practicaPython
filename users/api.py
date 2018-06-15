from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from users.permissions import UserPermission
from users.serializers import UserSerializer, UserListSerializer, UserBlogSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [UserPermission]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name']
    ordering_fields = ['first_name']

    def get_serializer_class(self):

        if self.action == 'create' or self.action == 'update':
            return UserSerializer
        elif self.action == 'retrieve':
            return UserSerializer
        elif self.action == 'list':
            return UserBlogSerializer
        else:
            return UserListSerializer


