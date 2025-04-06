from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES = (
    ('All','All'),
    ('Kids','Kids'),
)
MOVIE_CHOICES = (
    ('seasonal','Seasonal'),
    ('single','Single'),
)

class CustomUser(AbstractUser):
    # Add any additional fields you want for your custom user model
    profiles = models.ManyToManyField('Profile', blank=True, )

class Profile(models.Model):
    name = models.CharField(max_length=1000)
    AGE_CHOICES = models.CharField(max_length=10, choices=AGE_CHOICES,)
    uid = models.UUIDField(default=uuid.uuid4,)

    def __str__(self):  # Fixed space between def and __str__
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank = True, null = True)
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=MOVIE_CHOICES,)
    uid = models.UUIDField(default=uuid.uuid4,)
    video = models.ManyToManyField('Video', )
    image = models.ImageField(upload_to='covers', )
    age_choices = models.CharField(max_length=10, choices=AGE_CHOICES,)
   
    def __str__(self): # Fixed space between def and __str__
       return self.title

class Video(models.Model):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='movies',)
    
    def __str__(self):  # Fixed space between def and __str__
       return self.title
   