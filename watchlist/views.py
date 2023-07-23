from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    data = {"movies":list(movies.values())}
    # data1= data["movies"][0]
    return JsonResponse(data)

def movie_details(request,pk):
    movie = Movie.objects.get(pk=pk)
    data = {"name":movie.title,"description":movie.description,"active":movie.active}
    return JsonResponse(data)
    
