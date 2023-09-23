from django.db import models
from django import forms
class add_resources(models.Model):
    RESOURCE_CHOICES = [
        (1, 'Resource Type'),
        (2, 'Theory'),
        (3, 'Lab'),
    ]
    email=models.CharField( max_length=122)
    Department=models.CharField( max_length=12,default='None')
    type = models.IntegerField(choices=RESOURCE_CHOICES, default=1) 
    Course=models.CharField(max_length=9,default='Not label')  #file name
    file= models.FileField(upload_to='',default='No file given')  #uploaded file
    texxt=models.CharField( max_length=200)
    
    

    def __str__(self):
        return self.Course
    def getType(self):
        if self.type==2:
            return 'Theory'
        else:
            return 'lab'
    

class faculty(models.Model):
    g_suit=models.CharField( max_length=122)
    initial=models.CharField( max_length=12,default='None')
    room_no=models.CharField(max_length=9,default='NO room assigned') 
    file= models.FileField(upload_to='faculty',default='No file given')  
  
    def __str__(self):
        return self.initial
    