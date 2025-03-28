from django.db import models
import datetime
import uuid

choices1=[
    ('N','None'),
    ('D','Daily'),
    ('W','Weekly'),
    ('M','Monthly'),
    ('Y','Yearly')
]

class User(models.Model):

    def __str__(self):
        return self.name
    
# user category ka figure out
    
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
    recurrence=models.TextField(max_length=220, choices=choices1)
    recur_start=models.DateField(default=datetime.date.today,null=True, blank=True)
    recur_end=models.DateField(default=datetime.date.today, null=True, blank=True)
    def __str__(self):
        return self.name