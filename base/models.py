from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

class Users(models.Model):
    TYPE = (
        ('S', 'Student'),
        ('E', 'Elder'),
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE, primary_key=True  
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)    
    type = models.CharField(max_length=1, choices=TYPE)
    birth_date = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    profile_pic = models.ImageField(null = True, upload_to='images')
    class Meta:
         db_table = 'base_users'
    remaining_hours = models.IntegerField(default=True)




# class Chores(models.Model):
    
#     elder_id = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE, 
#     )
#     chore_id = models.AutoField(max_length=200, primary_key=True)
#     chore_date = models.CharField(max_length=200)
#     chore_time = models.CharField(max_length=200)
#     description = models.TextField()


#     class Meta:
#          db_table = 'base_chores'
 

