from django.views.generic import TemplateView, ListView
from .models import Category, Period, Expense, Investment

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class CategoryPageView(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'all_categories_list'

class PeriodPageView(ListView):
    model = Period
    template_name = 'periods.html'
    context_object_name = 'all_periods_list'

class ExpensePageView(ListView):
    # ToDo: Filter expenses by Period
    model = Expense
    template_name = 'expenses.html'
    context_object_name = 'all_expenses_list'

class InvestmentPageView(ListView):
    model = Investment
    template_name = 'investments.html'
    context_object_name = 'all_investments_list'