from django.urls import path
from .views import HomeView, PrivacyView, AboutUsView, NewsView, NewsDetailView


# app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('privacy/', PrivacyView.as_view(), name='privacy')
]
