from django.shortcuts import render
from .serializers import MovieSerializer
from .models import Movie
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
      movies = Movie.objects.all()
      serializer = MovieSerializer(movies, many=True)
      return Response(serializer.data)
    elif request.method == 'POST':
      serializer = MovieSerializer(data=request.data)
      # if serializer:
      #   return Response({'error': 'This movie is already exist'})
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
  if request.method == 'GET':
    movies = Movie.objects.get(id=pk)
    serializer = MovieSerializer(movies, many=False)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    movies = Movie.objects.get(id=pk)
    serializer = MovieSerializer(instance=movies, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)
  
  elif request.method == 'DELETE':
    movies = Movie.objects.get(id=pk)
    movies.delete()
    return Response('Item successfully deleted!')