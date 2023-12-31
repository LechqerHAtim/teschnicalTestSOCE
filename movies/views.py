from rest_framework import viewsets
from .models import Actor, Movie, Review
from .serializers import ActorSerializer, MovieSerializer, ReviewSerializer
from django.shortcuts import render
from .tasks import simulate_cpu_intensive_task
from rest_framework.views import APIView
from rest_framework.response import Response
class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

#just to simulate the  celerey process
class SimulateTaskView(APIView):
    
    def get(self, request, *args, **kwargs):
        task_result = simulate_cpu_intensive_task.delay().get()  # Trigger the Celery task and wait for the result
        return Response(task_result)