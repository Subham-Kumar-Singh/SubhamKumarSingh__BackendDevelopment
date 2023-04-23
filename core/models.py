from django.db import models
# from django.db.models import /

# Create your models here.
class TradeDetails(models.Model):
    buy_sell_indicator = models.CharField(max_length=4, help_text="A value of BUY for buys, SELL for sells.")
    price = models.FloatField(help_text="The price of the Trade.")
    quantity = models.IntegerField(help_text="The amount of units traded.")

Option1=(
    ('buy',"BUY"),
    ('sell',"SELL"),
)

Option2=(
    ('amazon',"AMZN"),
    ('tesla',"TSLA"),
    ('alibaba',"ALBAB"),
    ('apple',"APPL"),
)

class Trade(models.Model):
    asset_class = models.CharField(max_length=255, null=True, blank=True, help_text="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc",choices=Option1)
    counterparty = models.CharField(max_length=255, null=True, blank=True, help_text="The counterparty the trade was executed with. May not always be available",)
    instrument_id = models.CharField(max_length=255, help_text="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc",choices=Option2)
    instrument_name = models.CharField(max_length=255, help_text="The name of the instrument traded.")
    trade_date_time = models.DateTimeField(help_text="The date-time the Trade was executed")
    trade_details = models.ForeignKey(TradeDetails, on_delete=models.CASCADE, help_text="The details of the trade, i.e. price, quantity")
    trade_id = models.CharField(max_length=255, null=True, blank=True, help_text="The unique ID of the trade")
    trader = models.CharField(max_length=255, help_text="The name of the Trader")
