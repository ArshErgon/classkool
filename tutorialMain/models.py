from django.db import models

# Create your models here.

from django.template.defaultfilters import slugify


class TutorialModel(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, verbose_name="Slug", unique=True)
    body = models.TextField(max_length=250)
    date_of_published = models.DateField(auto_now_add=True)

    def slug(self):
        return slugify(self.title)


    def __str__(self):
        return self.title
