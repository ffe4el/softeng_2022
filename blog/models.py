from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30) #제목 글자수 제한 30
    content = models.TestField()  #콘텐트는 블로그 글

    created_at = models.DateTimeField()
    #author: 추후 작성 예정
