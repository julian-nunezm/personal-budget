from django.views.generic import TemplateView, ListView
from .models import Category

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class CategoryPageView(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'all_categories_list'