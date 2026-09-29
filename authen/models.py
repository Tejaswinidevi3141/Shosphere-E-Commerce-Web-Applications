from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProfilePic(models.Model):
    profile = models.ImageField(upload_to='uploads/',default='OIP_8.webp')
    user =models.ForeignKey(User,on_delete=models.CASCADE)