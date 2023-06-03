from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_recipe')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")
    category = models.CharField(max_length=100)
    level = models.IntegerField()
    tool = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return self.name


class Element(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    put = models.IntegerField()
    unit = models.CharField(max_length=100)
    
    
class Cooking(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    process = models.TextField()


class Detail(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_detail')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    score = models.IntegerField()
    content = models.TextField()

# Create your models here.
