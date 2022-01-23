from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import Post


class PostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        post = super().create(validated_data)
        post.author = CurrentUserDefault()
        post.save()
        return post

    class Meta:
        model = Post
        fields = ('id', 'title', 'description')
