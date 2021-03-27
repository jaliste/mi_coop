from django.shortcuts import render
from .models import BasketSubscription
from django.views.generic.edit import CreateView, UpdateView
from rest_framework import viewsets
from .serializers import PickupDaySerializer, BasketSubscriptionSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ..membership.models import CoopMember
from .models import PickupDay

class PickupDayViewSet(viewsets.ModelViewSet):
    queryset = PickupDay.objects.all()
    serializer_class = PickupDaySerializer

class BasketSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = BasketSubscription.objects.all()
    serializer_class = BasketSubscriptionSerializer
