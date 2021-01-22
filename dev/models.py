from django.db import models
from django.contrib.auth.models import User
from cloudinary import  models as md

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='no bio yet.')
    profile_pic = md.CloudinaryField('image', null=True, blank=True)
    contact = models.EmailField() 

    def __str__(self):
        return str(self.user.username)

class Projects(models.Model):
    developer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.TextField() 
    image = md.CloudinaryField('image', null=True, blank=True) 
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return str(self.title)  
