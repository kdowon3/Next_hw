from django.db import models
from django.conf import settings



class Post(models.Model):
   title = models.CharField(max_length=50)
   content = models.TextField()
   creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
   last_viewed_time = models.DateTimeField(null=True, blank=True)
   last_viewed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)


   def __str__(self):
       return self.title
   
class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
   content = models.TextField()
   creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments", default=1 )

   def __str__(self):
       return self.content

