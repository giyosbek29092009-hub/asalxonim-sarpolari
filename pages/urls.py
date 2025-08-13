from django.urls import path
from .views import HomePageView, AboutPageView, html_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('html/', html_view, name='html'),

]