from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=200, blank=True)
    twitter_link = models.URLField(max_length=200, blank=True)
    google_plus_link = models.URLField(max_length=200, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name