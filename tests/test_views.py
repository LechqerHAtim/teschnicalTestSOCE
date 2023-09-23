from django.test import TestCase, Client
from django.urls import reverse
from movies.models import Actor, Movie, Review

class MovieViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.movie = Movie.objects.create(title='Test Movie', description='Test Description')

    def test_movie_list_view(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Movie')
