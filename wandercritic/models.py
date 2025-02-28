from django.db import models
from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# class Place(models.Model):
# 	pid = models.AutoField(primary_key=True)
# 	pname = models.CharField(max_length=50, unique=True)
# 	about = models.CharField(max_length=300)
# 	picture = models.ImageField()
# 	address = models.CharField(max_length=300)
# 	geolocation = models.CharField(max_length=30, default='default_value') 
# 	seasons = models.CharField(max_length=30)
# 	activity = models.CharField(max_length=30)
# 	travel_theme = models.CharField(max_length=30)
# 	budget = models.IntegerField(default=0)
# 	description = models.CharField(max_length=300)
	
# 	def __str__(self):
# 		return self.pname

# class Tour(models.Model):
# 	tname = models.CharField(max_length=50, unique=True)
# 	place = models.ForeignKey(Place, on_delete=models.CASCADE)
# 	information = models.CharField(max_length=128)
# 	picture = models.ImageField()
# 	address = models.CharField(max_length=300)
# 	price = models.IntegerField(default=0)
	
# 	def __str__(self):
# 		return self.tname
	
# class Review(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	pid = models.ForeignKey(Place, on_delete=models.CASCADE)
# 	rate = models.IntegerField()
# 	description = models.CharField(max_length=300)

# 	def __str__(self):
# 		return f"Review by {self.user.username}"
	
# class Admin(models.Model): 
# 	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# 	def __str__(self):
# 		return self.user.username 

class User(AbstractUser):
	# pass
    full_name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.username
    
# class UserProfile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
# 	profile = models.ImageField(upload_to='profile_pics')

# 	def __str__(self):
# 		return self.user.username

# class TravelAgent(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.user.username 


# class AdminPlaceManage(models.Model):
# 	admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
# 	place = models.ForeignKey(Place, on_delete=models.CASCADE)

# class TravelAgentTourManage(models.Model):
# 	ta = models.ForeignKey(TravelAgent, on_delete=models.CASCADE)
# 	tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

# class UserPlaceView(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	place = models.ForeignKey(Place, on_delete=models.CASCADE)

