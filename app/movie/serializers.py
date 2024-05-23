from rest_framework import serializers
from core.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields=['id', 'title', 'director', 'duration']
        read_only_fields = ['id']

class MovieDetailSerializer(MovieSerializer):
    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields +['rating', 'main_character', 'description']