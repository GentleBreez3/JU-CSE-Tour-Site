from django.db import models
from django.urls import reverse

class Money(models.Model):
    name = models.CharField(max_length=256)
    amount = models.IntegerField()
    batch = models.IntegerField()
    roll  = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(Money,related_name='students',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
