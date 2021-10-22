from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class userProfile(models.Model):
    CHOICES = (
        ('পুরুষ', 'পুরুষ'),
        ('মহিলা', 'মহিলা'),
        ('অন্যান্য', 'অন্যান্য'),
        
    )
    CHOICE = (
        ('ইসলাম', 'ইসলাম'),
        ('সনাতন', 'সনাতন'),
        ('বৌদ্ধ', 'বৌদ্ধ'),
        ('খ্রিষ্টান', 'খ্রিষ্টান'),
        ('অন্যান্য', 'অন্যান্য'),
        
    )
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    dateOfBirth = models.DateField()
    nationality = models.CharField(max_length=100,default="বাংলাদেশী")
    bio = models.CharField(max_length=300,default=" ")
    height = models.CharField(max_length=50,default=" ")
    weight = models.CharField(max_length=50,default=" ")
    religion = models.CharField(max_length=50,choices = CHOICE,default="")
    sex = models.CharField(max_length=20, choices = CHOICES,default="")
    proffession = models.CharField(max_length=200,default=" ")
    phone = models.CharField(max_length=15,default="")
    profilePicture = models.ImageField(default = 'profilepics/default.png', upload_to = 'profilepics')
    galleryPicOne = models.ImageField(default = 'profilepics/default.png', upload_to = 'gallerypics')
    galleryPicTwo = models.ImageField(default = 'profilepics/default.png', upload_to = 'gallerypics')
    galleryPicThree = models.ImageField(default = 'profilepics/default.png', upload_to = 'gallerypics')
    galleryPicFour = models.ImageField(default = 'profilepics/default.png', upload_to = 'gallerypics')
    
    def __str__(self):
        return f'{self.user.username} profile'
    
