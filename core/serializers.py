from .models import *

from rest_framework import serializers

class TradeDeatilSerializer(serializers.ModelSerializer):
    class Meta:
        model=TradeDetails
        fields="__all__"


class TradeSerializer(serializers.ModelSerializer):
    trade_details=TradeDeatilSerializer()
    class Meta:
        model=Trade
        fields="__all__"