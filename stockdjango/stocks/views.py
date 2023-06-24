from django.shortcuts import render
# Create your views here.
import requests
import json

def home(request):

    try:
        ticker = request.GET['ticker']
        stock_api = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_1beff6d0b97b4cfcac54956d551dd530")
        stock = json.loads(stock_api.content)
    except Exception as e:
        stock = ""

    content = {'stock':stock}

    return render(request, 'stocks/home.html', content)