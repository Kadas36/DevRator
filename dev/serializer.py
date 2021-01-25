from rest_framework import serializers
from .models import Profile,Project,Review, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'profile', 'is_active', 'is_staff', 'is_superuser')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user', 'bio', 'profile_pic', 'contact')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','developer', 'title', 'image', 'description', 'link')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('reviewer', 'project', 'comment', 'design_rating', 'usability_rating', 'content_rating')                 