import requests
from django.views.generic import TemplateView, DetailView
from .models import News

API_URL = 'https://fast-api-7gqj.onrender.com'

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
            if not News.objects.filter(url=url).exists():
                News.objects.create(url=url, is_translated=False)

        context = super().get_context_data(**kwargs)
        context["context"] = News.objects.all()
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
