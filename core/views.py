from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .serializers import *
from .views import *

from django.views.decorators.csrf import csrf_protect

from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt


from django_filters.rest_framework import DjangoFilterBackend, RangeFilter
from django_filters import rest_framework
# Create your views here.

@csrf_exempt
def Home(request):
    if request.method == 'POST':
        trade_id = request.POST['trade_id']
        try:
            trade = Trade.objects.get(trade_id=trade_id)
            serializer = TradeSerializer(trade)
            return render(request, 'core/trade_detail.html', {'data': dict(serializer.data)})
        except Trade.DoesNotExist:
            return HttpResponse('Invalid Trade ID')
    else:
        trades = Trade.objects.all()
        return render(request, 'core/home.html', {'trades': trades})

@csrf_exempt
class TradeDetailView(APIView):
    def get(self, request, trade_id):
        try:
            trade = Trade.objects.get(trade_id=trade_id)
            serializer = TradeSerializer(trade)
            return Response(serializer.data)
        except Trade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TradeAll(generics.ListAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer


class SearchTrade(generics.ListAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['counterparty',
                     'instrument_id', 'instrument_name', 'trader']


class TradeFilter(rest_framework.FilterSet):
    trade_details__price = rest_framework.RangeFilter()
    trade_date_time = rest_framework.RangeFilter()

    class Meta:
        model = Trade
        fields = ['instrument_id', 'asset_class',
                  'trade_details__price', 'trade_date_time']


class TradeList(generics.ListAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['instrument_id', 'asset_class']
    filterset_class = TradeFilter


class TradeOrder(generics.ListAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = "__all__"
