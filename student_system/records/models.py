from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    admission_date = models.DateField()

    def __str__(self):
        return self.name
