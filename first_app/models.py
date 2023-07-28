from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique = True)
    
    def __str__(self):
        return self.top_name
    

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()
    
    
    def __str__(self):
        return str(self.date)
    
class Users(models.Model):
    f_name = models.CharField(max_length= 30)
    l_name = models.CharField(max_length= 30)
    email = models.EmailField(max_length=50, unique=True)
    
    def __str__(self):
        return self.f_name + " " + self.l_name
    
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #aditional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return self.user.username
    
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    
    
    def __str__(self):
        return self.name
    
class Students(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    