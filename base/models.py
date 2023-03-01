from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

now = timezone.localtime(timezone.now()).time()
now_with_seconds = now.strftime("%H:%M:%S")

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
        ('09:00', '09:00'),
        ('09:30', '09:30'),
        ('10:00', '10:00'),
        ('10:30', '10:30'),
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),
        ('15:30', '15:30'),
        ('16:00', '16:00'),
        ('16:30', '16:30'),
        ('17:00', '17:00'),
    )
    TIME = ( ('1', '1'), ('2', '2'), ('3', '3'),('4', '4'),)
    STATUS = (( 'Pending', 'Pending'), ('Registed', 'Registed'), ('Done', 'Done'),)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    student_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='student_id')
    title = models.CharField(max_length=200)
    description = models.TextField( primary_key=True)
    date= models.CharField(max_length=200)
    start_hour = models.CharField(max_length=5, choices=HOUR)
    time = models.CharField(max_length=200, choices=TIME)
    status = models.CharField(max_length=200, choices=STATUS, default='Pending')
    creation_time = models.CharField(max_length=200, default= now_with_seconds)
    class Meta:
         db_table = 'base_chores'
