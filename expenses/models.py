from django.db import models

class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Expense(models.Model):
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField()

# ToDo: Create Period and check what others Classes could be created. Budget?