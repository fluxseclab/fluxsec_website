import requests
from django.views.generic import TemplateView
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
        url_list = requests.get(API_URL).json()['urls']
        for url in url_list:
            if News.objects.filter(url=url).exists() == False:
                response = requests.get(f'{API_URL}/scrape?url={url}').json()

                try:
                    url = response['url']
                    content = response['content']
                except:
                    break

                News.objects.create(url=url, content=content)

        context = super(NewsView, self).get_context_data(**kwargs)
        context["context"] = News.objects.all()
        return context
