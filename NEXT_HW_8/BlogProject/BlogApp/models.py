from django.db import models
from django.utils import timezone

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('hobby', '취미'),
        ('food', '음식'),
        ('programming', '프로그래밍'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # 기본값 설정
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


