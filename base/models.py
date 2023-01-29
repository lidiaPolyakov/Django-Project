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
    TIME = (('30 min', '30 min'), ('1 hour', '1 hour'),  ('1.5 hour', '1.5 hour'), ('2 hours', '2 hours'), ('2.5 hours', '2.5 hours'), ('3 hours', '3 hours'),)
    STATUS = (( 'Pending', 'Pending'), ('Registed', 'Registed'), ('Done', 'Done'),)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    student_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='student_id')
    #chore_id = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date= models.CharField(max_length=200)
    start_hour = models.CharField(max_length=5, choices=HOUR)
    time = models.CharField(max_length=200, choices=TIME)
    status = models.CharField(max_length=200, choices=STATUS, default='Pending')
    creation_time = models.DateTimeField(primary_key=True, default= timezone.now())
    class Meta:
         db_table = 'base_chores'
