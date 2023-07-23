from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=100)
    description=serializers.CharField(max_length=1000)
    active=serializers.BooleanField(default=True)

    # Create a new movie object
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    # Check if the movie already exists in the database
    def validate(self, data):
        title = data.get('title')
        existing_movie = Movie.objects.filter(title=title).first()
        if existing_movie:
            raise serializers.ValidationError('This movie already exists.')
        return data
    
    # Update an existing movie object
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance