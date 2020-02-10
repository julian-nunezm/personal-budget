from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from .models import Category

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(name='Test', description='This is a description.')
    
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
        self.assertEqual(expected_object_name, 'Test')