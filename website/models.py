from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    subject = models.TextField(max_length=100)
    message = models.CharField(max_length=500)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.email


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone_number = PhoneNumberField()
    check_in = models.DateTimeField()
    n_people = models.IntegerField()
    subject = models.TextField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.email
