from django.urls import path
from .views import HomePageView, AboutPageView, CategoryPageView, PeriodPageView, ExpensePageView, InvestmentPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('categories/', CategoryPageView.as_view(), name='categories'),
    path('periods/', PeriodPageView.as_view(), name='periods'),
    path('expenses/', ExpensePageView.as_view(), name='expenses'), # ToDo: Include Period to filter by.
    path('investments/', InvestmentPageView.as_view(), name='investments'),
]
