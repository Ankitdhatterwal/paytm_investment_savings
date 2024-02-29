from rest_framework import serializers
from .models import FinancialProduct, Transaction, DMateAccount, Company, StockPrice

class FinancialProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialProduct
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'



class DMateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DMateAccount
        fields = '__all__'


        

class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrice
        fields = ['price', 'timestamp']

class CompanySerializer(serializers.ModelSerializer):
    stock_prices = StockPriceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Company
        fields = ['name', 'stock_prices']