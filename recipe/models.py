from django.db import models
from datetime import datetime
from people.models import Person

class Recipe(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    prepare_time = models.IntegerField()
    serves = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
