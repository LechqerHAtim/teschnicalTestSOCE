from django.db import models
#add all models with relation between them
#___--___
class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class Meta:
        app_label = 'movies'  
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    actors = models.ManyToManyField(Actor)
    class Meta:
        app_label = 'movies'  

    def __str__(self):
        return self.title

class Review(models.Model):
    grade = models.PositiveIntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    class Meta:
        app_label = 'movies'  
    def __str__(self):
        return f'Review for {self.movie.title}'
