from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.CharField(max_length=122)
    date = models.DateField()
    def __str__(self):
        return self.email

class Exercise(models.Model):
    exercise_name= models.CharField(max_length=200)
    price = models.IntegerField()
    trainer = models.CharField(max_length=200)

    def __str__ (self):
        return self.exercise_name