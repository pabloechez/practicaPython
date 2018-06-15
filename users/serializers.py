from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        view_name = "api-blogs:users-detail"
        fields = ['id', 'username']


class UserBlogSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse('api-posts-mine', kwargs={'id': obj.id})

    class Meta:
        model = User
        view_name = 'users:user-detail'
        fields = ['username', 'first_name', 'url']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User()
        return self.update(user, validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username')
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.email= validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, username):
        if (self.instance is None or self.instance.username != username) and User.objects.filter(username=username).exists():
            raise ValidationError('Ya existe un usuario con ese username')

        return username
