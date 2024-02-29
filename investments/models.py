from django.db import models

from django.contrib.auth.models import User

class FinancialProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(FinancialProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class DMateAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    bank_name = models.CharField(max_length=100)

    def __str__(self):
        return f"DMate Account for {self.user.username}"

        

class Company(models.Model):
    name = models.CharField(max_length=100)

class StockPrice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField()