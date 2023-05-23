from rest_framework import serializers
from codeBase.models import *

# JGold Services Serializer
class GiftCardSerializer(serializers.ModelSerializer):
    class Meta: 
        model = GiftCardModel
        fields = "__all__"

class CryptoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CryptoModel
        fields = "__all__"

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TestimonialModel
        fields = "__all__"