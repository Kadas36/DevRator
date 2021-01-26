from django.db import models
from django.contrib.auth.models import User
from cloudinary import  models as md
from django.forms.fields import Field

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='no bio yet.')
    profile_pic = md.CloudinaryField('image', null=True, blank=True)
    contact = models.EmailField() 

    def __str__(self):
        return str(self.user.username)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
 
    def update_profile(self,new_profile):
        self.profile_pic = new_profile.profile_pic
        self.bio = new_profile.bio
        self.contact = new_profile.contact
        self.save()      
    

class Project(models.Model):
    developer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.TextField() 
    image = md.CloudinaryField('image', null=True, blank=True) 
    description = models.TextField()
    link = models.URLField()


    def __str__(self):
        return str(self.title)  

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    
class Review(models.Model):
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    design_rating = models.FloatField(default=1)
    usability_rating = models.FloatField(default=1)
    content_rating = models.FloatField(default=1)

    def __str__(self):
        return str(self.reviewer.user.username)

    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()    

