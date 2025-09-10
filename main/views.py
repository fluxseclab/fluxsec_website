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

    def get_context_data(self, **kwargs):
        
        url_list = requests.get(API_URL).json().get('urls', [])
        
        for url in url_list:
            news_obj = News.objects.filter(url=url).first()

            try:
                response = requests.get(f'{API_URL}/scrape?url={url}').json()
                content = response['content'].replace('\n', '').strip()
            except Exception as e:
                print(f"Error fetching {url}: {e}")
                continue

            if news_obj is None:
                News.objects.create(url=url, content=content, is_translated=True)
            
            elif not news_obj.is_translated:
                news_obj.content = content
                news_obj.is_translated = True
                news_obj.save()

        context = super(NewsView, self).get_context_data(**kwargs)
        context["context"] = News.objects.all()
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'