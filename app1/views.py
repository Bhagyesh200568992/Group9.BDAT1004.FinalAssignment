from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import datetime
import requests
import time
import pytz
from pymongo import MongoClient
from urllib.parse import quote_plus
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.utils import timezone
import json


def home(request):
    return render(request,'index.html')


def alldata(request):

    username = "bhagyeshparmar28"
    password = "Bhagyesh@123"

    # Escape the username and password
    escaped_username = quote_plus(username)
    escaped_password = quote_plus(password)

    # Construct the MongoDB connection string using f-string
    mongo_uri = f"mongodb+srv://{escaped_username}:{escaped_password}@grp9.so9fs9r.mongodb.net/crypto?ssl=true&ssl_cert_reqs=CERT_NONE"
    client = MongoClient(mongo_uri)
    db = client.get_database('crypto')
    records = db.price

    a = list(records.find({}, {
        "btcinr": {'low': 1, 'high': 1, 'last': 1, 'open': 1, 'volume': 1, 'sell': 1, 'buy': 1, 'at': 1}}))
    dic={'data':a}
    print(dic)
    return render(request,'table.html',dic)


def g1(request):

    # Your MongoDB credentials
    username = "bhagyeshparmar28"
    password = "Bhagyesh@123"

    # Escape the username and password
    escaped_username = quote_plus(username)
    escaped_password = quote_plus(password)

    # Construct the MongoDB connection string using f-string
    mongo_uri = f"mongodb+srv://{escaped_username}:{escaped_password}@grp9.so9fs9r.mongodb.net/crypto?ssl=true&ssl_cert_reqs=CERT_NONE"
    client = MongoClient(mongo_uri)
    db = client.get_database('crypto')
    records = db.price

    a = list(records.find({}, {
        "btcinr": {'low': 1, 'high': 1, 'last': 1, 'open': 1, 'volume': 1, 'sell': 1, 'buy': 1, 'at': 1}}))


    # Extract timestamps and 'last' values for 'btcinr'
    timestamps = [timezone.datetime.utcfromtimestamp(item['btcinr']['at']) for item in a]




    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_dt =  [i.astimezone(ist_timezone).strftime('%m-%d %H:%M') for i in timestamps]




    last_values = [float(item['btcinr']['open']) for item in a]

    context = {'time': ist_dt, 'price': last_values,'title':"Price Of Bitcoin in INR for 1 Minute Timeframe",'color':'rgb(255, 102, 102, 1)'}

    return render(request, 'chartjs.html', context)


def g2(request):

    # Your MongoDB credentials
    username = "bhagyeshparmar28"
    password = "Bhagyesh@123"

    # Escape the username and password
    escaped_username = quote_plus(username)
    escaped_password = quote_plus(password)

    # Construct the MongoDB connection string using f-string
    mongo_uri = f"mongodb+srv://{escaped_username}:{escaped_password}@grp9.so9fs9r.mongodb.net/crypto?ssl=true&ssl_cert_reqs=CERT_NONE"
    client = MongoClient(mongo_uri)
    db = client.get_database('crypto')
    records = db.price


    b = list(records.find({}, {
        "ethinr": {'low': 1, 'high': 1, 'last': 1, 'open': 1, 'volume': 1, 'sell': 1, 'buy': 1, 'at': 1}}))

    # Extract timestamps and 'last' values for 'btcinr'

    timestamps = [timezone.datetime.utcfromtimestamp(item['ethinr']['at']) for item in b]

    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_dt = [i.astimezone(ist_timezone).strftime('%m-%d %H:%M') for i in timestamps]

    last_values = [float(item['ethinr']['open']) for item in b]

    context = {'time': ist_dt, 'price': last_values,'title':"Price Of Ethereum in INR for 1 Minute Timeframe",'color':'rgb(0, 163, 254, 1)'}

    return render(request, 'chartjs.html', context)


def g3(request):

    # Your MongoDB credentials
    username = "bhagyeshparmar28"
    password = "Bhagyesh@123"

    # Escape the username and password
    escaped_username = quote_plus(username)
    escaped_password = quote_plus(password)

    # Construct the MongoDB connection string using f-string
    mongo_uri = f"mongodb+srv://{escaped_username}:{escaped_password}@grp9.so9fs9r.mongodb.net/crypto?ssl=true&ssl_cert_reqs=CERT_NONE"
    client = MongoClient(mongo_uri)
    db = client.get_database('crypto')
    records = db.price


    c = list(records.find({}, {
        "maticinr": {'low': 1, 'high': 1, 'last': 1, 'open': 1, 'volume': 1, 'sell': 1, 'buy': 1, 'at': 1}}))

    # Extract timestamps and 'last' values for 'btcinr'

    timestamps = [timezone.datetime.utcfromtimestamp(item['maticinr']['at']) for item in c]

    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_dt = [i.astimezone(ist_timezone).strftime('%m-%d %H:%M') for i in timestamps]

    last_values = [float(item['maticinr']['open']) for item in c]

    context = {'time': ist_dt, 'price': last_values,'title':"Price Of Matic Coin in INR for 1 Minute Timeframe",'color':'rgb(21, 72, 29, 1)'}

    return render(request, 'chartjs.html', context)


def g4(request):
    # Your MongoDB credentials
    username = "bhagyeshparmar28"
    password = "Bhagyesh@123"

    # Escape the username and password
    escaped_username = quote_plus(username)
    escaped_password = quote_plus(password)

    # Construct the MongoDB connection string using f-string
    mongo_uri = f"mongodb+srv://{escaped_username}:{escaped_password}@grp9.so9fs9r.mongodb.net/crypto?ssl=true&ssl_cert_reqs=CERT_NONE"
    client = MongoClient(mongo_uri)
    db = client.get_database('crypto')
    records = db.price

    a = list(records.find({}, {
        "btcinr": {'low': 1, 'high': 1, 'last': 1, 'open': 1, 'volume': 1, 'sell': 1, 'buy': 1, 'at': 1}}))

    b = list(records.find({}, {
        "ethinr": {'low': 1, 'high': 1, 'last': 1, 'open': 1, 'volume': 1, 'sell': 1, 'buy': 1, 'at': 1}}))

    volumes1 = [float(item['btcinr']['volume']) for item in a]
    total_volume1 = sum(volumes1)

    volumes2 = [float(item['ethinr']['volume']) for item in b]
    total_volume2 = sum(volumes2)
    # Pie chart
    labels = [ 'btc/INR','eth/inr']
    sizes = [ total_volume1,total_volume2]
    colors = ['lightcoral', 'lightskyblue']
    context = {'t1': total_volume1, 't2': total_volume2, 'title': "Volume Distribution",
               }

    return render(request, 'pie.html', context)


def g5(request):
    # Your MongoDB credentials
    username = "bhagyeshparmar28"
    password = "Bhagyesh@123"

    # Escape the username and password
    escaped_username = quote_plus(username)
    escaped_password = quote_plus(password)

    # Construct the MongoDB connection string using f-string
    mongo_uri = f"mongodb+srv://{escaped_username}:{escaped_password}@grp9.so9fs9r.mongodb.net/crypto?ssl=true&ssl_cert_reqs=CERT_NONE"
    client = MongoClient(mongo_uri)
    db = client.get_database('crypto')
    records = db.price

    a = list(records.find({}, {
        "btcinr": {'low': 1, 'high': 1, 'last': 1, 'open': 1, 'volume': 1, 'sell': 1, 'buy': 1, 'at': 1}}))

    b = list(records.find({}, {
        "ethinr": {'low': 1, 'high': 1, 'last': 1, 'open': 1, 'volume': 1, 'sell': 1, 'buy': 1, 'at': 1}}))

    c = list(records.find({}, {
        "maticinr": {'low': 1, 'high': 1, 'last': 1, 'open': 1, 'volume': 1, 'sell': 1, 'buy': 1, 'at': 1}}))

    def calculate_total_traded_price(record):
        return float(record['btcinr']['last']) * float(record['btcinr']['volume'])

    def calculate_total_traded_price1(record):
        return float(record['ethinr']['last']) * float(record['ethinr']['volume'])

    def calculate_total_traded_price2(record):
        return float(record['maticinr']['last']) * float(record['maticinr']['volume'])

    # Calculate total traded price for BTC/INR across all records
    total_traded_price_btcinr = sum([calculate_total_traded_price(record) for record in a])
    total_traded_price_ethinr = sum([calculate_total_traded_price1(record1) for record1 in b])
    total_traded_price_maticinr = sum([calculate_total_traded_price2(record2) for record2 in c])

    # Bar chart
    labels = ['BTC/INR', 'ETH', 'matic']
    total_traded_prices = [total_traded_price_btcinr, total_traded_price_ethinr, total_traded_price_maticinr]
    colors = ['lightcoral', 'lightblue', 'lightgreen']

    context={'t1':total_traded_price_btcinr,'t2':total_traded_price_ethinr,'t3':total_traded_price_maticinr}

    return render(request, 'chart.html', context)
