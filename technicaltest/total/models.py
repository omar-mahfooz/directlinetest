from django.db import models
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from rest_framework import serializers
# Create your models here.



class Total(models.Model):
    numbers_to_add = list(range(10000001))

    total = models.IntegerField()

    def __unicode__(self):
        return "Total: %s" %self.total

