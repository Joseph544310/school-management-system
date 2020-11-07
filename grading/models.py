from django.db import models
from draftapp.models import Student


class Grade(models.Model):

    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Semester = models.IntegerField(default=1)
    Math_Grade = models.FloatField(default=0.0)
    Physics_Grade = models.FloatField(default=0.0)
    Chemistry_Grade = models.FloatField(default=0.0)
    English_Grade = models.FloatField(default=0.0)
    Arabic_Grade = models.FloatField(default=0.0)
    History_Grade = models.FloatField(default=0.0)
    Geography_Grade = models.FloatField(default=0.0)
    Tarbiya_Grade = models.FloatField(default=0.0)
    Average = models.FloatField(default=0.0)

    class Meta:
        unique_together = (("Student", "Semester"),)

