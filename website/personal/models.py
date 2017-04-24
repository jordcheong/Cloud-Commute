from django.db import models

# Create your models here.

#Syracuse University
class work_location(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

class route(models.Model):
    work = models.ForeignKey(work_location, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    current_location = models.CharField(max_length=100)
