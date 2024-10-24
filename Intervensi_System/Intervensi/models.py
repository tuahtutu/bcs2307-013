from django.db import models

# Create your models here.
class Problem(models.Model):
   Report_id=models.AutoField(primary_key=True)
   Staff_id = models.IntegerField(max_length=7)
   Student_id = models.CharField(max_length=12)
