from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta, time
import random
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    profile_pic = models.ImageField(default='profile_pics/default.jpg',upload_to='profile_pics')
    bio = models.TextField(null=True , blank=True ,max_length=500,default="")

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-id']


class Schedule(models.Model):
    Weeks =(
        ('1', 'Week1'),
        ('2', 'Week2'),
        ('3', 'Week3'),
        ('4', 'Week4'),
    )
    Week_days =(
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
    )
    Schedule_Type =(
        ('Study','Study'),
        ('Health','Health')
    )
    
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    week = models.CharField(max_length=100, choices=Weeks)
    week_days = models.CharField(max_length=100, choices=Week_days)
    type = models.CharField(max_length=100, choices=Schedule_Type)
    task = models.CharField(max_length=100)
    duration = models.TimeField()

    def str(self):
        return f'{self.task}-{self.parent}'
    

    #     unique_together = week, day_of_week, parent

    

@receiver(post_save, sender=User)
def create_schedule_for_new_user(sender, instance, created, **kwargs):
    day_mapping = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
    }
    subject_mapping = {
        1: 'English',
        2: 'Math',
        3: 'Physics',
        4: 'Computer',
        5: 'Psychology',
        6: 'Lab',
    }
    sport_mapping = {
        1: 'Cardio',
        2: 'Cricket',
        3: 'Football',
        4: 'Yoga',
        5: 'Swimming',
        6: 'Hiking',
    }
    time_mapping = {
    1: time(9, 0),    # 9:00 AM
    2: time(10, 0),   # 10:00 AM
    3: time(11, 0),   # 11:00 AM
    4: time(12, 0),   # 12:00 PM
    5: time(12, 30),  # 12:30 PM
    6: time(12, 59)   # 12:59 PM
}
    if created:
        current_date = datetime.now()
        week_count = 1
        for i in range(1, 5):
            for value in range(1, 7):
                day = day_mapping.get(value)
                subject = subject_mapping.get(value)
                sport = sport_mapping.get(value)
                duration = time_mapping.get(value)
                # random_hour = random.randint(8, 14)
                # duration = datetime.combine(current_date, datetime.min.time()) + timedelta(hours=random_hour)
                if week_count == 1 or week_count == 2:
                    Schedule.objects.create(parent=instance, week=f"{week_count}", week_days=day, type="Study", task=subject, duration=duration)
                else:
                    Schedule.objects.create(parent=instance, week=f"{week_count}", week_days=day, type="Health", task=sport, duration=duration)
                
            
            week_count += 1