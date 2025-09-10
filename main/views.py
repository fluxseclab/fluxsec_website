import asyncio
import aiohttp
import requests
from django.views.generic import TemplateView, DetailView
from .models import News

API_URL = 'https://flux-fast-api.onrender.com'

class HomeView(TemplateView):
    template_name = 'home.html'


class PrivacyView(TemplateView):
    template_name = 'privacy.html'


class AboutUsView(TemplateView):
    template_name = 'about_us.html'


class NewsView(TemplateView):
    template_name = 'news.html'

    async def fetch_content(self, session, url):
        try:
            async with session.get(f'{API_URL}/scrape?url={url}') as resp:
                data = await resp.json()
                content = data['content'].replace('\n', '').strip()
                return url, content
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return url, None

    async def fetch_all(self, urls):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_content(session, url) for url in urls]
            return await asyncio.gather(*tasks)

    def get_context_data(self, **kwargs):
        url_list = requests.get(API_URL).json().get('urls', [])

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(self.fetch_all(url_list))

        for url, content in results:
            if not content:
                continue

            news_obj = News.objects.filter(url=url).first()
            if news_obj is None:
                News.objects.create(url=url, content=content, is_translated=True)
            elif not news_obj.is_translated:
                news_obj.content = content
                news_obj.is_translated = True
                news_obj.save()

        context = super().get_context_data(**kwargs)
        context["context"] = News.objects.all()
        return context



class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'