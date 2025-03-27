from django.db import models
from datetime import datetime

class User(models.Model):

    def __str__(self):
        return self.name
    
#user category ka figure out
    
class Event(models.Model):

    def __str__(self):
        return self.name