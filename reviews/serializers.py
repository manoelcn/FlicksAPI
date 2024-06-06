from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

    def validate_comment(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O seu comentário não pode exceder 200 caracteres.')
        return value


class ReviewListDetailSerializer(serializers.ModelSerializer):
    movie_title = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'movie_title', 'stars', 'comment']

    def get_movie_title(self, obj):
        return obj.movie.title
