from django.db import models
from django.forms import forms


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dob = models.DateTimeField()
    email = models.EmailField(unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    is_spoty = models.BooleanField(default=False)
    kcpe_score = models.IntegerField()
    profile_pic = models.ImageField(upload_to='students', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}  {self.last_name} "
# when add field please make migration.
# python manage.py makemigtation
# python manage.py migrate and import pillow
