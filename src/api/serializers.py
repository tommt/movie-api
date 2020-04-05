from rest_framework import serializers

from .models import Movie, Rating


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movie
        fields = ("id", "title", "descriptions")


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model= Rating
        fields = ("id", "stars", "user", "movie")
        