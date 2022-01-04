from django.db import models


# Create your models here.
class Madan(models.Model):
    name = models.CharField(max_length=125)
    location = models.CharField(max_length=125)
    description = models.TextField()
    stone_type = models.CharField(max_length=125)
    country = models.CharField(max_length=125)
    city = models.CharField(max_length=125)
    province = models.CharField(max_length=125)
    state = models.CharField(max_length=125)

    def __str__(self):
        return self.name