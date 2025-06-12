from rest_framework import viewsets, permissions, authentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Pharmacy, InventoryItem, Sale, Order, WebhookEvent
from .serializers import PharmacySerializer, InventoryItemSerializer, SaleSerializer, OrderSerializer, WebhookEventSerializer

class APIKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-KEY')
        if not api_key:
            return None
        try:
            pharmacy = Pharmacy.objects.get(api_key=api_key, is_active=True)
        except Pharmacy.DoesNotExist:
            raise AuthenticationFailed('Invalid or inactive API key')
        return (pharmacy, None)

class PharmacyViewSet(viewsets.ModelViewSet):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class WebhookEventViewSet(viewsets.ModelViewSet):
    queryset = WebhookEvent.objects.all()
    serializer_class = WebhookEventSerializer
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [permissions.IsAuthenticated]
