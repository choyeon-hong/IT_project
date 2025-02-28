from django.db import models
from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Place(models.Model):
	pname = models.CharField(max_length=50, unique=True)
	about = models.CharField(max_length=300)
	picture = models.ImageField()
	address = models.CharField(max_length=300)
	seasons = models.CharField(max_length=30)
	activity = models.CharField(max_length=30)
	travel_theme = models.CharField(max_length=30)
	budget = models.IntegerField(default=0)
	reviews = models.CharField(max_length=300)
	username = models.CharField(max_length=30)
	rate = models.IntegerField(default=5)
	description = models.CharField(max_length=300)
	
	def __str__(self):
		return self.pname

class Tour(models.Model):
	tname = models.CharField(max_length=50, unique=True)
	place = models.ForeignKey(Place, on_delete=models.CASCADE)
	information = models.CharField(max_length=128)
	picture = models.ImageField()
	address = models.CharField(max_length=300)
	price = models.IntegerField(default=0)
	
	def __str__(self):
		return self.tname
	

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username
	

class User(AbstractUser):
	# pass
    full_name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.username