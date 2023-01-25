from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

class Users(models.Model):
    TYPE = (
        ('S', 'Student'),
        ('E', 'Elder'),
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
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
    remaining_hours = models.IntegerField(default=250)


class Chore(models.Model):
    HOUR = (
        ('9', '09:00'),
        ('95', '09:30'),
        ('10', '10:0'),
        ('105', '10:30'),
        ('11', '11:00'),
        ('115', '11:30'),
        ('12', '12:00'),
        ('125', '12:30'),
        ('13', '13:00'),
        ('135', '13:30'),
        ('14', '14:00'),
        ('145', '14:30'),
        ('15', '15:00'),
        ('155', '15:30'),
        ('16', '16:00'),
        ('166', '16:30'),
        ('17', '17:00'),
    )
    TIME = (('1', '30 min'), ('2', '1 hour'),  ('3', '1.5 hour'), ('4', '2 hours'), ('5', '2.5 hours'), ('6', '3 hours'),)
    STATUS = (('P', 'Pending'), ('R', 'Registed'), ('D', 'Done'),)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    student_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='student_id')
    chore_id = models.IntegerField(default=1, primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date= models.CharField(max_length=200)
    start_hour = models.CharField(max_length=5, choices=HOUR)
    time = models.CharField(max_length=200, choices=TIME)
    status = models.CharField(max_length=200, choices=STATUS, default='P')
    creation_time = models.DateTimeField(default= timezone.now())
    class Meta:
         db_table = 'base_chores'
