from django.db import models


# Create your models here.
class EmailSave(models.Model):
    subject = models.CharField(max_length=350)
    message = models.TextField(max_length= 1000)

    def __str__(self):
        return self.subject
