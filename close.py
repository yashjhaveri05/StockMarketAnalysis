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
    plt.title('For Google Stock')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Close Price', fontsize=14)
    plt.grid(True)
    plt.show()
    if(diff_google < 0):
        print(f"Google has seen a fall in stock value of ${abs(diff_google)} as compared to stock value on {start.date()}")
    else:
        print(f"Google has seen a rise in stock value of ${abs(diff_google)} as compared to stock value on {start.date()}")

def oracle_func():
    start = dt.datetime(2015, 11, 27)
    end = dt.datetime.now()
    oracle = web.DataReader("ORCL", 'yahoo', start, end)
    diff_oracle = int(oracle['Close'][-1] - oracle['Close'][0])
    plt.plot(oracle.index,oracle['Close'])
    plt.title('For Oracle Stock')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Close Price', fontsize=14)
    plt.grid(True)
    plt.show()
    if(diff_oracle < 0):
        x = f"oracle has seen a fall in stock value of ${abs(diff_oracle)} as compared to stock value on {start.date()}"
    else:
        x = f"oracle has seen a rise in stock value of ${abs(diff_oracle)} as compared to stock value on {start.date()}"

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

def infosys_func():
    start = dt.datetime(2015, 11, 27)
    end = dt.datetime.now()
    infosys = web.DataReader("INFY.NS", 'yahoo', start, end)
    diff_infosys = int(infosys['Close'][-1] - infosys['Close'][0])
    plt.plot(infosys.index,infosys['Close'])
    plt.title('For Infosys Stock')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Close Price', fontsize=14)
    plt.grid(True)
    plt.show()
    if(diff_infosys < 0):
        print(f"infosys has seen a fall in stock value of ${abs(diff_infosys)} as compared to stock value on {start.date()}")
    else:
        print(f"infosys has seen a rise in stock value of ${abs(diff_infosys)} as compared to stock value on {start.date()}")

def tcs_func():
    start = dt.datetime(2015, 11, 27)
    end = dt.datetime.now()
    tcs = web.DataReader("TCS.NS", 'yahoo', start, end)
    diff_tcs = int(tcs['Close'][-1] - tcs['Close'][0])
    plt.plot(tcs.index,tcs['Close'])
    plt.title('For TCS Stock')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Close Price', fontsize=14)
    plt.grid(True)
    plt.show()
    if(diff_tcs < 0):
        print(f"tcs has seen a fall in stock value of ${abs(diff_tcs)} as compared to stock value on {start.date()}")
    else:
        print(f"tcs has seen a rise in stock value of ${abs(diff_tcs)} as compared to stock value on {start.date()}")

def combination():
    start = dt.datetime(2015, 11, 27)
    end = dt.datetime.now()
    google = web.DataReader("GOOGL", 'yahoo', start, end)
    microsoft = web.DataReader("MSFT", 'yahoo', start, end)
    oracle = web.DataReader("ORCL", 'yahoo', start, end)
    tcs = web.DataReader("TCS.NS", 'yahoo', start, end)
    infosys = web.DataReader("INFY.NS", 'yahoo', start, end)

    stock_list = [google, microsoft, oracle, tcs, infosys]

    for df in stock_list:
        df.reset_index(inplace=True)
        df.set_index("Date", inplace=True)
        df.drop(['High','Low','Open','Volume','Adj Close'],axis=1,inplace=True)

    plt.plot(google.index,google['Close'], label = "Google")
    plt.plot(microsoft.index,microsoft['Close'], label = "Microsoft")
    plt.plot(oracle.index,oracle['Close'], label = "Oracle")
    plt.plot(tcs.index,tcs['Close'], label = "TCS")
    plt.plot(infosys.index,infosys['Close'],label = "Infosys")

    plt.title('Close Price vs Year', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Close Price', fontsize=14)
    plt.grid(True)
    plt.legend() 
    plt.show()