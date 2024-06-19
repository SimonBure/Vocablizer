from django.db import models

class English(models.Model):
    word = models.fields.CharField(max_length=100)
    meaning = models.fields.CharField(max_length=100, blank=True)
    example = models.fields.CharField(max_length=100, blank=True)
