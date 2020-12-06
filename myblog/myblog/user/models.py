from django.db import models
from django import forms
import os
# Create your models here.
from django.test import TestCase
from django.utils.timezone import now

# Create your tests here.
class user( models.Model ):
    id = models.AutoField('id', primary_key=True, editable=False)
    name = models.CharField('namne', max_length=100, blank=True)
    email_addr =  forms.EmailField(label="Email", widget=forms.EmailInput)
    head_img = models.CharField('head_img_path', max_length=256, blank=True)
    c_time =  models.DateTimeField('c_time', default=now)
    arrts =  models.PositiveIntegerField('attrs', default=0)

def f():
    pass