from django.db import models
import datetime
import uuid

RECURRENCE_CHOICES=[
    ('N','None'),
    ('D','Daily'),
    ('W','Weekly'),
    ('M','Monthly'),
    ('Y','Yearly')
]

DEPARTMENT_CHOICES = [
        ('AE', 'Aerospace Engineering'),
        ('BB', 'Biosciences and Bioengineering'),
        ('CE', 'Chemical Engineering'),
        ('CH', 'Chemistry'),
        ('CE', 'Civil Engineering'),
        ('CSE', 'Computer Science & Engineering'),
        ('ES', 'Earth Sciences'),
        ('EE', 'Electrical Engineering'),
        ('ESE', 'Energy Science and Engineering'),
        ('ESED', 'Environmental Science and Engineering'),
        ('HSS', 'Humanities & Social Science'),
        ('IEOR', 'Industrial Engineering & Operations Research'),
        ('MA', 'Mathematics'),
        ('ME', 'Mechanical Engineering'),
        ('ME', 'Metallurgical Engineering & Materials Science'),
        ('PH', 'Physics'),
        ('IDC', 'Industrial Design Centre'),
        ('SOM', 'Shailesh J. Mehta School of Management'),
        ('Other', 'Other')
    ]

DEGREE_CHOICES = [
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('PhD', 'PhD'),
        ('MS', 'MS'),
        ('MBA', 'MBA'),
        ('M.Des', 'M.Des'),
        ('M.Sc', 'M.Sc'),
        ('MA', 'MA'),
        ('B.Des', 'B.Des'),
        ('B.Sc', 'B.Sc'),
        ('BA', 'BA'),
        ('Other', 'Other')
    ]

USER_GROUP_CHOICES=[
    ('C','Club'),
    ('TT','Tech Team'),
    ('Co', 'Community'),
    ('O','Others')
]


class UserCategory(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.TextField(max_length=20, choices=USER_GROUP_CHOICES,default='club')
    bodies=models.JSONField(default=list, blank=True)
    def __str__(self):
        return self.name


class Body(models.Model):
  name = models.CharField(max_length=100)
  type = models.IntegerField(choices=USER_GROUP_CHOICES)
  contact_email = models.EmailField()
  def __str__(self):
      return self.name


class User(models.Model):
    name = models.CharField(max_length=100, default='')
    roll_number=models.CharField(max_length=20, default='')
    department=models.CharField(choices=DEPARTMENT_CHOICES, max_length=100, default='CE')
    degree=models.CharField( choices=DEGREE_CHOICES, max_length=100 ,default='B.Tech')
    user_category=models.ManyToManyField(UserCategory)
    body=models.ManyToManyField(Body)
    def __str__(self):
        return self.name
    

class Event(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.TextField(max_length=100, null=True)
    description=models.TextField(max_length=200, null=True, blank=True)
    organiser=models.TextField(max_length=20)
    venue=models.TextField(max_length=20, null=True)
    start_time=models.TimeField(default=datetime.datetime.now(), null=True, blank=True)
    end_time=models.TimeField(default=datetime.datetime.now(), null=True, blank=True)
    start_date=models.DateField(default=datetime.date.today)
    end_date=models.DateField(default=datetime.date.today)
    recurrence=models.TextField(max_length=220, choices=RECURRENCE_CHOICES)
    recur_start=models.DateField(default=datetime.date.today,null=True, blank=True)
    recur_end=models.DateField(default=datetime.date.today, null=True, blank=True)
    def __str__(self):
        return self.name