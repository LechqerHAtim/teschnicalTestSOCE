from rest_framework.routers import DefaultRouter
from .views import ActorViewSet, MovieViewSet, ReviewViewSet

router = DefaultRouter()

router.register(r'actors', ActorViewSet, basename='actor')
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = router.urls
