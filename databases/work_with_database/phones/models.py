from django.db import models
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(max_length=254, null=False)
    price = models.IntegerField(null=False)
    image = models.ImageField()
    release_date = models.DateField(null=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=254, unique=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('phone', args=[self.slug])
