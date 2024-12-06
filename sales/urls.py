from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Saleviewset

router = DefaultRouter()
router.register(r'sales',Saleviewset,basename='sale')

urlpatterns = [
    path('',include(router.urls))
]
