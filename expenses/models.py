from django.db import models

class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Period(models.Model):
    # Choices for Period.status
    OPEN = 'OP'
    CLOSED = 'CL'
    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (CLOSED, 'Closed'),
        # ToDo: Analyze how to manage a planned period to compare against the open one. How would it work with the projection periods?
    ]
    # Attributes
    name = models.CharField(primary_key=True, max_length=7)
    category_by_period = models.ManyToManyField(Category, db_table='category_by_period', related_name='periods')
    category_amount_by_period = models.FloatField(default=0.0)  # ToDo: This field should be in the many-to-many relation table, not in Period.
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=OPEN)

    def __str__(self):
        return self.name

    def is_open(self):
        return self.status == self.OPEN

class Expense(models.Model):
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField()

class Investment(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    creation_period = models.ForeignKey(Period, on_delete=models.CASCADE)
    total_amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

# ToDo: Create Period and check what others Classes could be created. Budget?
# ToDo: Create a model for Projects, and Debts.
# ToDo: Create a new app for my Loans business.