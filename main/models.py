from django.db import models


class News(models.Model):
    url = models.CharField(max_length=200)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.content[:50]
    