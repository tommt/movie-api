from django.shortcuts import render
from rest_framework import viewsets

from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializers


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = (MovieSerializer,)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = (RatingSerializers, )

