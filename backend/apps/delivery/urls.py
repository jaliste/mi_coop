from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pickup', views.PickupDayViewSet)
router.register(r'subscription', views.BasketSubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
