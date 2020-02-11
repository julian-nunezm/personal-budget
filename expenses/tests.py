from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from .models import Category, Period, Expense, Investment
from datetime import datetime

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(name='Test Category', description='This is a description.')
    
    def test_categories_url_exists_at_proper_location(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
    
    def test_categories_url_by_name(self):
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)
    
    def test_categories_url_uses_the_correct_template(self):
        response = self.client.get(reverse('categories'))
        self.assertTemplateUsed(response, 'categories.html')

    def test_category_name(self):
        category = Category.objects.get(description='This is a description.')
        expected_object_name = f'{category.name}'
        self.assertEqual(expected_object_name, 'Test Category')

class PeriodModelTest(TestCase):
    def setUp(self):
        Period.objects.create(name='2020-01')
    
    def test_periods_url_exists_at_proper_location(self):
        response = self.client.get('/periods/')
        self.assertEqual(response.status_code, 200)
    
    def test_periods_url_by_name(self):
        response = self.client.get(reverse('periods'))
        self.assertEqual(response.status_code, 200)
    
    def test_periods_url_uses_the_correct_template(self):
        response = self.client.get(reverse('periods'))
        self.assertTemplateUsed(response, 'periods.html')
    
    def test_period_initial_status(self):
        period = Period.objects.get(name='2020-01')
        expected_object_status = f'{period.status}'
        self.assertTrue(expected_object_status in (period.OPEN, period.CLOSED))
        self.assertEqual(expected_object_status, period.OPEN)

class ExpenseModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Category 1')
        Expense.objects.create(date=datetime.now(), category=category, amount=15.95, description='Test Expense')
    
    def test_expenses_url_exists_at_proper_location(self):
        response = self.client.get('/expenses/')
        self.assertEqual(response.status_code, 200)
    
    def test_expenses_url_by_name(self):
        response = self.client.get(reverse('expenses'))
        self.assertEqual(response.status_code, 200)
    
    def test_expenses_url_uses_the_correct_template(self):
        response = self.client.get(reverse('expenses'))
        self.assertTemplateUsed(response, 'expenses.html')
    
    def test_expense_category(self):
        expense = Expense.objects.get(amount=15.95)
        expected_object_category = f'{expense.category}'
        self.assertEqual(expected_object_category, 'Category 1')

class InvestmentModelTest(TestCase):
    def setUp(self):
        period = Period.objects.create(name='2020-02')
        Investment.objects.create(name='Test Investment', creation_period=period)
    
    def test_investments_url_exists_at_proper_location(self):
        response = self.client.get('/investments/')
        self.assertEqual(response.status_code, 200)
    
    def test_investments_url_by_name(self):
        response = self.client.get(reverse('investments'))
        self.assertEqual(response.status_code, 200)
    
    def test_investments_url_uses_the_correct_template(self):
        response = self.client.get(reverse('investments'))
        self.assertTemplateUsed(response, 'investments.html')
    
    def test_investment_category(self):
        investment = Investment.objects.get(name='Test Investment')
        expected_object_period = f'{investment.creation_period}'
        self.assertEqual(expected_object_period, '2020-02')