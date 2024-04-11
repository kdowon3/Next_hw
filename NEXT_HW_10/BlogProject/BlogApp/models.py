from django.db import models
from django.utils import timezone

class Post(models.Model):
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
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    
    def __str__(self):
        return self.content
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
