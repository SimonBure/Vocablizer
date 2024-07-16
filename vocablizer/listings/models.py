from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class English(models.Model):

    class Genre(models.TextChoices):
        NOUN = 'NOUN'
        VERB = 'VERB'
        ADJECTIVE = 'ADJECTIVE'
        ADVERB = 'ADVERB'
        PRONOUN = 'PRONOUN'
        PREPOSITION = 'PREPOSITION'
        CONJUNCTION = 'CONJUNCTION'
        INTERJECTION = 'INTERJECTION'

    word = models.fields.CharField(max_length=100)
    meaning = models.fields.CharField(max_length=100, blank=True)
    rank = models.fields.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    active = models.fields.BooleanField(default=True)
    genre = models.fields.CharField(max_length=100, choices=Genre.choices)
    genre = models.fields.CharField(max_length=100, choices=Genre.choices)
    created_at = models.fields.DateTimeField(auto_now_add=True)
    updated_at = models.fields.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.word} ({self.genre})" 
    
class Example(models.Model):
    english = models.ForeignKey(English, on_delete=models.CASCADE, null=True) # null = True, because we want to allow examples without English words
    example = models.fields.CharField(max_length=100)
    created_at = models.fields.DateTimeField(auto_now_add=True)
    updated_at = models.fields.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.example}"