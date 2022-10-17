import json
import requests
import pandas
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
try:
    import yfinance as yf
except ImportError:
    print("Missing Yahoo Finance, try pip install yfinance")
    
try:
    import utils
except ImportError:
    print("try pip install utils")

def display_info(stock):
    json_info = {}
    data = yf.Ticker(stock)
    info = data.info
    print("Name Ticker:", data.ticker)
    json_info["Name Ticker"] = data.ticker
    
    print("Full Name of Stock:", info["longName"])
    json_info["Full Name of Stock"] = info["longName"]

    print("Current Name:", info["currentPrice"])
    json_info["Current Name"] = info["currentPrice"]

    print("Target Mean Price:", info["targetMeanPrice"])
    json_info["Target Mean Price"] = info["targetMeanPrice"]

    print("Cash on Hand:", info["totalCash"])
    json_info["Cash on Hand"] = info["totalCash"]

    print("Profit Margins:", info["profitMargins"])
    json_info["Profit Margins"] = info["profitMargins"]

    print("Time Pulled:", datetime.now())
    json_info["Time Pulled"] = str(datetime.now())

    return json_info


def write_json(json_info, stock):
    stock_info = stock + "info.json"
    with open(stock_info, 'w') as json_file:
        json.dump(json_info, json_file)

def time_list(x):
    x_ = str(x).split()[0]
    return(x_.split("-"))

def select():
    today = datetime.now()
    five_ago = today - timedelta(days=5)
    a = time_list(five_ago)
    b = time_list(today)
    return [a,b]


def plot_5_days(stock):
    data = yf.Ticker(stock)

    startDate= datetime(int(select()[0][0]),int(select()[0][1]),int(select()[0][2]))
    endDate= datetime(int(select()[1][0]),int(select()[1][1]),int(select()[1][2]))
    
    past_5_days = data.history(start=startDate,end=endDate)
    past_5_days["Close"].plot(title=stock+" stock price")
    print()
    print(past_5_days["Close"])
    plt.ylabel("Closing price ($)")
    print("Five days ago was:",startDate)
