from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""class employee(models.Model):
    enmae=models.CharField(max_length=30)
    eno=models.IntegerField()
    esal=models.FloatField()"""


"""def __str__(self):
    return self.enmae"""

class userprofileinfo(models.Model):
    user= models.OneToOneField(User,on_delete=models.DO_NOTHING)

    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True )

    def __str__(self):
        return self.user