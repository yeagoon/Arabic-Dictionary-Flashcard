from django.db import models

# Create your models here.


class SearchHistory(models.Model):
    search_word = models.CharField(max_length=40)


class ContentList(models.Model):
    arabic_word = models.CharField(max_length=40)
    definition1 = models.TextField()
    definition2 = models.TextField(blank=True, null=True)
    definition3 = models.TextField(blank=True, null=True)
    definition4 = models.TextField(blank=True, null=True)
    definition5 = models.TextField(blank=True, null=True)


class CurrentFlashcard(models.Model):
    current_index = models.IntegerField()
