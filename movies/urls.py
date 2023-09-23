from rest_framework.routers import DefaultRouter
from .views import ActorViewSet, MovieViewSet, ReviewViewSet
from .views import SimulateTaskView
from django.urls import path

router = DefaultRouter()

router.register(r'actors', ActorViewSet, basename='actor')
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    # ... (your existing URLs)
    path('simulate_task/', SimulateTaskView.as_view(), name='simulate_task'),
]
urlpatterns = router.urls+urlpatterns
