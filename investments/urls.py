from django.urls import path
from rest_framework import status
from .views import FinancialProductList, TransactionCreate
from .views import DMateAccountCreate,CompanyStockPriceList


urlpatterns = [
    path('products/', FinancialProductList.as_view(), name='product-list'),
    path('transactions/create/', TransactionCreate.as_view(), name='transaction-create'),
     path('dmate-accounts/create/', DMateAccountCreate.as_view(), name='dmate-account-create'),
      path('api/companies/', CompanyStockPriceList.as_view(), name='company-stock-prices'),

]


