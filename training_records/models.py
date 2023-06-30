from django.db import models


# Create your models here.
class Training(models.Model):
    activity = models.CharField(max_length=200)
    training_date = models.DateTimeField('date trained')

    def __str__(self):
        return self.activity
