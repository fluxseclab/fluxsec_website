from django.db import models


class News(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=250, default='تایتیل وارد نشده است !')
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    is_translated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.content[:250]
    
