
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=50, blank=True, default="")

    def __str__(self):
        return self.name


class Company(models.Model):
    comp_name = models.CharField(max_length=50, default="Null")
    comp_email = models.EmailField(
        blank=True,
        default="null@example.com"
    )
    location = models.CharField(max_length=50, default="Null")
    branch_no = models.IntegerField(default=1)

    @property
    def name(self):
        return self.comp_name

    def __str__(self):
        return self.comp_name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
