from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.forms.fields import DateTimeField
 
# Create your models here.

class user(User):
    pass

    def __str__(self):
        return self.username
    
    
class Post(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(default=datetime.now())
    updated_at=models.DateTimeField(default=datetime.now())
    
    
    def __str__(self):
        return self.text
    def __str__(self):
        return self.updated_at
    def __str__(self):
        return self.created_at