from django.core.management.base import BaseCommand
from ...models import News
from bs4 import BeautifulSoup
import requests

API_URL = "https://flux-fast-api.onrender.com"

class Command(BaseCommand):
    help = "Process ONE untranslated news item"

    def handle(self, *args, **kwargs):
        news_obj = News.objects.filter(is_translated=False).first()

        if not news_obj:
            self.stdout.write(self.style.SUCCESS("No untranslated news found."))
            return

        try:
            response = requests.get(f"{API_URL}/scrape?url={news_obj.url}").json()
            content = response.get("content", "").replace("\n", "").strip()

            if content == "":
                self.stderr.write(self.style.ERROR(f"No content for {news_obj.url}"))
                return


            soup = BeautifulSoup(content, "html.parser")
            
            title = soup.find("h1")
            if title and title.text.strip():
                news_obj.title = title.text.strip()

            news_obj.content = content
            news_obj.is_translated = True
            news_obj.save()

            self.stdout.write(self.style.SUCCESS(f"Processed: {news_obj.url}"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error fetching {news_obj.url}: {e}"))
