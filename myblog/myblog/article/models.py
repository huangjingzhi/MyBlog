from django.db import models
from django.utils.timezone import now
from django import forms
from user.models import user
# Create your models here.
views = models.PositiveIntegerField('浏览量', default=0)

class article( models.Model ):
    id = models.AutoField('id', primary_key=True, editable=False)
    release_time =  models.DateTimeField('release_time', default=now)
    release_state = models.PositiveIntegerField('release_state', default=0)
    path = models.CharField('path', max_length=256, blank=True)
    read_count =  models.PositiveIntegerField('read_count', default=0)
    title = models.CharField('title', max_length=100, blank=True)
    teg_category =  models.PositiveIntegerField('teg_category', default=0)
    label_set = models.CharField('label_set', max_length=300, blank=True)
    author_name = models.CharField('name', max_length=100, blank=True)
    keywords = models.CharField('keywords', max_length=300)
    doc_format = models.CharField('doc_format', max_length=20, blank=True)
    
class comment( models.Model ):
    id = models.AutoField('id', primary_key=True, editable=False)
    c_time = models.DateTimeField('c_time', default=now)
    content = models.CharField('content', max_length=256, blank=True)
    # article_id = models.AutoField('article_id', editable=False)
    # reviewer_id =  models.AutoField('reviewer_id', editable=False) # user_id
    article_id = models.ForeignKey(article, on_delete=models.CASCADE)
    reviewer_id = models.ForeignKey( user, on_delete = models.CASCADE )