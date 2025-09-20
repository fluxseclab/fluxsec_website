from django.db import models
from bs4 import BeautifulSoup

class News(models.Model):
    url = models.CharField(max_length=200)
    content = models.TextField()
    is_translated = models.BooleanField(default=False)
    is_trend = models.BooleanField(default=False)
    is_critical = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        title = soup.find('h1')
        if title:
            return title.text

        return "تایتل وارد نشده است! محتوا را ببینید..."