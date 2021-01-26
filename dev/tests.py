from django.contrib.auth.forms import UsernameField
from django.test import TestCase
from .models import Profile,User,Project, Review

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        User.kadas= Profile(user = 'kadas')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kadas,Profile))  

    # Testing Save Method
    def test_save_method(self):
        self.kadas.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)       
