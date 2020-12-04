import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

def google_func():
    start = dt.datetime(2015, 11, 27)
    end = dt.datetime.now()
    google = web.DataReader("GOOGL", 'yahoo', start, end)
    diff_google = int(google['Close'][-1] - google['Close'][0])
    plt.plot(google.index,google['Close'])
    plt.title('For Alphabet Stock')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Close Price', fontsize=14)
    plt.grid(True)
    plt.show()
    if(diff_google < 0):
        print(f"Alphabet has seen a fall in stock value of ${abs(diff_google)} as compared to stock value on {start.date()}")
    else:
        print(f"Alphabet has seen a rise in stock value of ${abs(diff_google)} as compared to stock value on {start.date()}")

def facebook_func():
    start = dt.datetime(2015, 11, 27)
    end = dt.datetime.now()
    facebook = web.DataReader("FB", 'yahoo', start, end)
    diff_facebook = int(facebook['Close'][-1] - facebook['Close'][0])
    plt.plot(facebook.index,facebook['Close'])
    plt.title('For Facebook Stock')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Close Price', fontsize=14)
    plt.grid(True)
    plt.show()
    if(diff_facebook < 0):
        print(f"Facebook has seen a fall in stock value of ${abs(diff_facebook)} as compared to stock value on {start.date()}")
    else:
        print(f"Facebook has seen a rise in stock value of ${abs(diff_facebook)} as compared to stock value on {start.date()}")

def microsoft_func():
    start = dt.datetime(2015, 11, 27)
    end = dt.datetime.now()
    microsoft = web.DataReader("MSFT", 'yahoo', start, end)
    diff_microsoft = int(microsoft['Close'][-1] - microsoft['Close'][0])
    plt.plot(microsoft.index,microsoft['Close'])
    plt.title('For Microsoft Stock')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Close Price', fontsize=14)
    plt.grid(True)
    plt.show()
    if(diff_microsoft < 0):
        print(f"microsoft has seen a fall in stock value of ${abs(diff_microsoft)} as compared to stock value on {start.date()}")
    else:
        print(f"microsoft has seen a rise in stock value of ${abs(diff_microsoft)} as compared to stock value on {start.date()}")

def amazon_func():
    start = dt.datetime(2015, 11, 27)
    end = dt.datetime.now()
    amazon = web.DataReader("AMZN", 'yahoo', start, end)
    diff_amazon = int(amazon['Close'][-1] - amazon['Close'][0])
    plt.plot(amazon.index,amazon['Close'])
    plt.title('For Amazon Stock')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Close Price', fontsize=14)
    plt.grid(True)
    plt.show()
    if(diff_amazon < 0):
        print(f"Amazon has seen a fall in stock value of ${abs(diff_amazon)} as compared to stock value on {start.date()}")
    else:
        print(f"Amazon has seen a rise in stock value of ${abs(diff_amazon)} as compared to stock value on {start.date()}")

def ibm_func():
    start = dt.datetime(2015, 11, 27)
    end = dt.datetime.now()
    ibm = web.DataReader("IBM", 'yahoo', start, end)
    diff_ibm = int(ibm['Close'][-1] - ibm['Close'][0])
    plt.plot(ibm.index,ibm['Close'])
    plt.title('For IBM Stock')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Close Price', fontsize=14)
    plt.grid(True)
    plt.show()
    if(diff_ibm < 0):
        print(f"IBM has seen a fall in stock value of ${abs(diff_ibm)} as compared to stock value on {start.date()}")
    else:
        print(f"IBM has seen a rise in stock value of ${abs(diff_ibm)} as compared to stock value on {start.date()}")

def combination():
    start = dt.datetime(2015, 11, 27)
    end = dt.datetime.now()
    google = web.DataReader("GOOGL", 'yahoo', start, end)
    microsoft = web.DataReader("MSFT", 'yahoo', start, end)
    facebook = web.DataReader("FB", 'yahoo', start, end)
    ibm = web.DataReader("IBM", 'yahoo', start, end)
    amazon = web.DataReader("AMZN", 'yahoo', start, end)

    stock_list = [google, microsoft, facebook, ibm, amazon]

    for df in stock_list:
        df.reset_index(inplace=True)
        df.set_index("Date", inplace=True)
        df.drop(['High','Low','Open','Volume','Adj Close'],axis=1,inplace=True)

    plt.plot(google.index,google['Close'], label = "Alphabet")
    plt.plot(microsoft.index,microsoft['Close'], label = "Microsoft")
    plt.plot(facebook.index,facebook['Close'], label = "Facebook")
    plt.plot(ibm.index,ibm['Close'], label = "IBM")
    plt.plot(amazon.index,amazon['Close'],label = "Amazon")

    plt.title('Close Price vs Year', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Close Price', fontsize=14)
    plt.grid(True)
    plt.legend() 
    plt.show()