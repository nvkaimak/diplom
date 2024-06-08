from rest_framework import serializers

from posts.models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['photo']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    images = PostImageSerializer(many=True)
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes_count'] = instance.likes.count()
        return representation
