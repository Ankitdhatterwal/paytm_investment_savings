from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import FinancialProduct, Transaction, DMateAccount,Company,StockPrice
from .serializers import FinancialProductSerializer, TransactionSerializer,  DMateAccountSerializer,CompanySerializer,CompanySerializer, StockPriceSerializer




class FinancialProductList(generics.ListAPIView):
    queryset = FinancialProduct.objects.all()
    serializer_class = FinancialProductSerializer

class TransactionCreate(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        


class DMateAccountCreate(generics.CreateAPIView):
    serializer_class = DMateAccountSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class CompanyStockPriceList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        # Assuming 'timestamp' is a query parameter representing the time
        timestamp = self.request.query_params.get('timestamp', None)
        if timestamp:
            # Filter stock prices by the specified timestamp
            queryset = Company.objects.prefetch_related('stock_prices').filter(
                stock_prices__timestamp=timestamp
            )
        else:
            queryset = Company.objects.all()
        return queryset



        



class CompanyStockPriceList(APIView):
    def get(self, request):
        # Retrieve all companies with their stock prices
        companies = Company.objects.all()
        serialized_data = CompanySerializer(companies, many=True).data
        return Response(serialized_data)