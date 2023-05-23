from django.shortcuts import render
from rest_framework import viewsets, status
from .api.serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

# JGoldServices Views
class GiftCardViewSet(viewsets.ModelViewSet):
    queryset = GiftCardModel.objects.all()
    serializer_class = GiftCardSerializer
    parser_classes = (MultiPartParser, FormParser)
   
class CryptoViewSet(viewsets.ModelViewSet):
    queryset = CryptoModel.objects.all()
    serializer_class = CryptoSerializer
    parser_classes = (MultiPartParser, FormParser)
    
class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = TestimonialModel.objects.all()
    serializer_class = TestimonialSerializer
