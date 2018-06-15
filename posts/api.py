from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.permissions import PostPermissions
from posts.serializers import PostListSerializer, NewPostSerializer, PostDetailSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']
    ordering_fields = ['created_on']
    ordering = ['-created_on']

    def get_serializer_class(self):
        if self.action == 'create':
            return NewPostSerializer
        elif self.action == 'list':
            return PostListSerializer
        else:
            return PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class MyPostAPI(ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [PostPermissions]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(owner=self.kwargs['id'])

        return Post.objects.filter(owner=self.kwargs['id'], status='APR')

