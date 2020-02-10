from django.urls import path
from .views import HomePageView, AboutPageView, CategoryPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('categories/', CategoryPageView.as_view(), name='categories'),
]
