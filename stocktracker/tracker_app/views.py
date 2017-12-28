# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, renderers

from .models import Stock
from .serializers import StockSerializer

# for API Root
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'stocks': reverse('stock-list', request=request, format=format)
    })




#playing around with frontend
def index(request):
    stock_list = Stock.objects.order_by('symbol')[:100] #pulls first 100 stocks based on symbol ABC order
    stock_string = ', '.join([stock.symbol for stock in stock_list])
    response = "Here is a list of all stocks in our database:\n" + stock_string
    return HttpResponse(response)

def custom_method_test(request, query_string):
    response = "custom method received: %s"
    return HttpResponse(response % query_string)
