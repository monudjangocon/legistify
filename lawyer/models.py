from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user=models.OneToOneField(User)
    
    def __unicode__(self):
        return self.user.username
    
    
class Legal(models.Model):
    
    CHOICES = (
        ('D', 'Delhi'),
        ('M', 'Mumbai'),
        ('N', 'Noida'),
        ('G', 'Gurgaon'),
        
    )
    practice_areas=models.CharField(max_length=1,choices=CHOICES)
    
class BasicDetail(models.Model):
    summary=models.TextField(max_length=500)
    

class BarInfo(models.Model):
    profile_pic=models.ImageField(upload_to="img")
    
    
    
