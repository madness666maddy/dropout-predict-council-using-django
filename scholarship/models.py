from django.db import models

class Scholarship(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    eligibility = models.CharField(max_length=200)
    amount = models.IntegerField()
    category = models.CharField(max_length=100)  # SC / ST / OBC / General / Girls
    min_attendance = models.IntegerField(default=75)

    def __str__(self):
        return self.name
