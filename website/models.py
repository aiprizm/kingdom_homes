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
    phone = PhoneNumberField()
    check_in = models.DateTimeField()
    n_people = models.IntegerField()
    subject = models.TextField(max_length=100)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.email


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    testimonial = models.TextField(max_length=500)
    stars = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    order = models.IntegerField(null=True)

    def __str__(self):
        return f"testimonial from: {self.name}"


class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    short_desc = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="team_pictures/", null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)

    # social media
    twitter = models.CharField(max_length=200, default="#")
    facebook = models.CharField(max_length=200, default="#")
    instagram = models.CharField(max_length=200, default="#")
    linkedin = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.name

