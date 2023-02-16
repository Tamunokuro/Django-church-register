from django.db import models
from django.utils.translation import LANGUAGE_SESSION_KEY

# Create your models here.


class MemberRecord(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phonenumber = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)
    added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Member Records"

    def __str__(self):
        return self.firstname + " " + self.lastname
