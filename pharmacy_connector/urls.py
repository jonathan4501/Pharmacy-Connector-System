"""
URL configuration for pharmacy_connector project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import PharmacyViewSet, InventoryItemViewSet, SaleViewSet, OrderViewSet, WebhookEventViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

router = routers.DefaultRouter()
router.register(r'pharmacies', PharmacyViewSet)
router.register(r'inventory', InventoryItemViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'webhook-events', WebhookEventViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Pharmacy Connector API",
        default_version='v1',
        description="API documentation for the Pharmacy Connector",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
