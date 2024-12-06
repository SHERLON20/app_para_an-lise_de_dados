from rest_framework import viewsets
from .models import sale
from .serializers import Saleserializer

class Saleviewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = Saleserializer
    
    def get_queryset(self):
        queryset = sale.objects.all()
        start_data = self.request.query_params.get('start_data')
        end_data = self.request.query_params.get('end_data')
        product = self.request.query_params.get('product')
        
        if start_data:
            queryset = queryset.filter(data__gte=start_data)
        if end_data:
            queryset = queryset.filter(data__lte=end_data)
        if product:
            queryset = queryset.filter(produto__icontains=product)
        return queryset
            
