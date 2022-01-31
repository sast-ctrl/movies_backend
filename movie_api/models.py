from django.db import models
from datetime import datetime
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)
    genre = models.CharField(max_length=50)
    plot = models.TextField()

    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        ordering =  ('-release_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug' : self.slug
        }

        return reverse('movies', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)
