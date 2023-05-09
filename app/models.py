from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    descrption = models.TextField(null=True, blank=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    qty = models.TextField(null=True, blank= False)
    update = models.DateTimeField(auto_now=True)
    crated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.ForeignKey(Room, on_delete= models.CASCADE)
    updaed = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.body(models.Model)
    

class Message(models.Model):
    name = models.CharField(max_length= 200 )
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    room = models.ForeignKey(Room, on_delete= models.CASCADE)
