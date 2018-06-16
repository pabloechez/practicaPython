from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'text', 'created_on' ]


class NewPostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'image', 'category']


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
