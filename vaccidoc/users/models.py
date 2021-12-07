from django import forms
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user= models.OneToOneField(User,on_delete=models.CASCADE)
   
  def __str__(self):
      return f'{self.user.username} Profile'

  def save(self):
      super().save
        


class AssessmentForm(models.Model):
  username=models.CharField(max_length=100, default='0000000')
  age=models.CharField(max_length=100)
  vaccine=models.CharField(max_length=100)
  chronic=models.CharField(max_length=100)
  tenderness=models.CharField(max_length=100)
  symptoms=models.CharField(max_length=100)
  feeling=models.CharField(max_length=100)
  

