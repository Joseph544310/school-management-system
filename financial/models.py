from django.db import models
from django.contrib.auth.models import User
from draftapp.models import Student


class Tuition(models.Model):

    student = models.OneToOneField(Student, primary_key=True, on_delete=models.CASCADE)
    total = models.BigIntegerField()
    paid = models.BigIntegerField()
    unpaid = models.BigIntegerField()



class Expense(models.Model):
    description = models.CharField(max_length=200)
    value = models.BigIntegerField()
    date = models.DateField()

    def __str__(self):
        return self.description

