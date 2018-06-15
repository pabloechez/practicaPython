from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'image', 'text', 'created_on']


class NewPostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
