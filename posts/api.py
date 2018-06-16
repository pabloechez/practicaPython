from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.permissions import PostPermissions
from posts.serializers import PostListSerializer, NewPostSerializer, PostDetailSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [PostPermissions]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']
    ordering_fields = ['title', 'created_on']
    ordering = ['-created_on']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        if self.request.user.is_authenticated:
            return Post.objects.filter(owner=self.request.user)
        else:
            return Post.objects.filter(status='APR')

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return NewPostSerializer
        elif self.action == 'list':
            return PostListSerializer
        else:
            return PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        snippet = self.get_object()
        serializer = self.get_serializer(snippet, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class MyPostAPI(ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [PostPermissions]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']
    ordering_fields = ['created_on']
    ordering = ['-created_on']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(owner=self.kwargs['id'])

        return Post.objects.filter(owner=self.kwargs['id'], status='APR')

