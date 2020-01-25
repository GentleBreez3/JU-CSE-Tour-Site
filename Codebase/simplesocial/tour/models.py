from django.db import models
from django.urls import reverse

class Students(models.Model):
    name = models.CharField(max_length=256)
    batch = models.IntegerField()
    roll  = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tour:detail",kwargs={'pk':self.pk})
