from django.db import models

# Create your models here.


class WordRecord(models.Model):
    inflectionalWord = models.CharField(max_length=100)
    isVerb = models.NullBooleanField(default=None)
    isLastWord = models.BooleanField(default=False)
    prefix = models.CharField(max_length=100, null=True)
    suffix = models.CharField(max_length=100, null=True)
    stemWord = models.CharField(max_length=100, null=True)
    targetStemWord = models.CharField(max_length=100, null=True)
    isAmbiguous = models.BooleanField(default=True)
    comment = models.TextField(null=True)
