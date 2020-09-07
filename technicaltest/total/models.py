from django.db import models
# Create your models here.



class Total(models.Model):
    numbers_to_add = list(range(10000001))

    total = models.IntegerField()

    def __unicode__(self):
        return "Total: %s" %self.total

