from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_pushed = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null = True, blank = True)
    
    def __str__(self):
        return str(self.title)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url