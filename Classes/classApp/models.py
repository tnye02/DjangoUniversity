from django.db import models

class DjangoClasses(models.Model):      #Creates the Django Classes class as well as the fields necessary
    title = models.CharField(max_length=50)
    courseNo = models.IntegerField()
    instructor = models.CharField(max_length=75)
    duration = models.FloatField(max_length=20)
    djClasses = models.Manager()



