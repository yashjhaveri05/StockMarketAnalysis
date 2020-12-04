import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from datetime import date as dt

#Year 2016
s1 = '2015-12-31'
e1 = '2017-01-01'

#Year 2017
s2 = '2016-12-31'
e2 = '2018-01-01'

#Year 2018
s3 = '2017-12-31'
e3 = '2019-01-01'

#Year 2019
s4 = '2018-12-31'
e4 = '2020-01-01'

#Year 2020
s5 = '2019-12-31'
e5 = '2020-11-30'

#Closing Dates For Each Year
c1 = '2016-12-30'
c2 = '2017-12-29'
c3 = '2018-12-31'
c4 = '2019-12-31'
c5 = '2020-11-27'

#Opening Dates For Each Year
o1 = '2016-01-04'
o2 = '2017-01-03'
o3 = '2018-01-02'
o4 = '2019-01-02'
o5 = '2020-01-02'

def google():

    google = yf.Ticker("GOOGL").history(period="5y")
    
    #Framing Dataframe for each year
    df1 = google.loc[(google.index > s1) & (google.index < e1)]
    df2 = google.loc[(google.index > s2) & (google.index < e2)]
    df3 = google.loc[(google.index > s3) & (google.index < e3)]
    df4 = google.loc[(google.index > s4) & (google.index < e4)]
    df5 = google.loc[(google.index > s5) & (google.index < e5)]

    #Getting sum of dividends for each year
    x1 = df1['Dividends'].sum()
    x2 = df2['Dividends'].sum()
    x3 = df3['Dividends'].sum()
    x4 = df4['Dividends'].sum()
    x5 = df5['Dividends'].sum()

    #Return = Close at end of year - Open at start of same year + dividend throughout the year
    z1 = google.loc[c1]['Close']-google.loc[o1]['Open']+x1
    z2 = google.loc[c2]['Close']-google.loc[o2]['Open']+x2
    z3 = google.loc[c3]['Close']-google.loc[o3]['Open']+x3
    z4 = google.loc[c4]['Close']-google.loc[o4]['Open']+x4
    z5 = google.loc[c5]['Close']-google.loc[o5]['Open']+x5

    #Deleting all dataframes 
    del df1,df2,df3,df4,df5

    #New Dataframe with the year and returns
    data = [['2016', z1], ['2017', z2], ['2018', z3], ['2019',z4], ['2020',z5]] 
    df_google = pd.DataFrame(data, columns = ['Year', 'Return']) 
    return df_google

def microsoft():

    microsoft = yf.Ticker("MSFT").history(period="5y")

    df1 = microsoft.loc[(microsoft.index > s1) & (microsoft.index < e1)]
    df2 = microsoft.loc[(microsoft.index > s2) & (microsoft.index < e2)]
    df3 = microsoft.loc[(microsoft.index > s3) & (microsoft.index < e3)]
    df4 = microsoft.loc[(microsoft.index > s4) & (microsoft.index < e4)]
    df5 = microsoft.loc[(microsoft.index > s5) & (microsoft.index < e5)]

    x1 = df1['Dividends'].sum()
    x2 = df2['Dividends'].sum()
    x3 = df3['Dividends'].sum()
    x4 = df4['Dividends'].sum()
    x5 = df5['Dividends'].sum()

    z1 = microsoft.loc[c1]['Close']-microsoft.loc[o1]['Open']+x1
    z2 = microsoft.loc[c2]['Close']-microsoft.loc[o2]['Open']+x2
    z3 = microsoft.loc[c3]['Close']-microsoft.loc[o3]['Open']+x3
    z4 = microsoft.loc[c4]['Close']-microsoft.loc[o4]['Open']+x4
    z5 = microsoft.loc[c5]['Close']-microsoft.loc[o5]['Open']+x5

    del df1,df2,df3,df4,df5

    data = [['2016', z1], ['2017', z2], ['2018', z3], ['2019',z4], ['2020',z5]] 
    df_microsoft = pd.DataFrame(data, columns = ['Year', 'Return']) 
    return df_microsoft

def facebook():

    facebook = yf.Ticker("FB").history(period="5y")

    df1 = facebook.loc[(facebook.index > s1) & (facebook.index < e1)]
    df2 = facebook.loc[(facebook.index > s2) & (facebook.index < e2)]
    df3 = facebook.loc[(facebook.index > s3) & (facebook.index < e3)]
    df4 = facebook.loc[(facebook.index > s4) & (facebook.index < e4)]
    df5 = facebook.loc[(facebook.index > s5) & (facebook.index < e5)]

    x1 = df1['Dividends'].sum()
    x2 = df2['Dividends'].sum()
    x3 = df3['Dividends'].sum()
    x4 = df4['Dividends'].sum()
    x5 = df5['Dividends'].sum()

    z1 = facebook.loc[c1]['Close']-facebook.loc[o1]['Open']+x1
    z2 = facebook.loc[c2]['Close']-facebook.loc[o2]['Open']+x2
    z3 = facebook.loc[c3]['Close']-facebook.loc[o3]['Open']+x3
    z4 = facebook.loc[c4]['Close']-facebook.loc[o4]['Open']+x4
    z5 = facebook.loc[c5]['Close']-facebook.loc[o5]['Open']+x5

    del df1,df2,df3,df4,df5

    data = [['2016', z1], ['2017', z2], ['2018', z3], ['2019',z4], ['2020',z5]] 
    df_facebook = pd.DataFrame(data, columns = ['Year', 'Return']) 
    return df_facebook

def amazon():

    amazon = yf.Ticker("AMZN").history(period="5y")

    df1 = amazon.loc[(amazon.index > s1) & (amazon.index < e1)]
    df2 = amazon.loc[(amazon.index > s2) & (amazon.index < e2)]
    df3 = amazon.loc[(amazon.index > s3) & (amazon.index < e3)]
    df4 = amazon.loc[(amazon.index > s4) & (amazon.index < e4)]
    df5 = amazon.loc[(amazon.index > s5) & (amazon.index < e5)]

    x1 = df1['Dividends'].sum()
    x2 = df2['Dividends'].sum()
    x3 = df3['Dividends'].sum()
    x4 = df4['Dividends'].sum()
    x5 = df5['Dividends'].sum()

    z1 = amazon.loc[c1]['Close']-amazon.loc[o1]['Open']+x1
    z2 = amazon.loc[c2]['Close']-amazon.loc[o2]['Open']+x2
    z3 = amazon.loc[c3]['Close']-amazon.loc[o3]['Open']+x3
    z4 = amazon.loc[c4]['Close']-amazon.loc[o4]['Open']+x4
    z5 = amazon.loc[c5]['Close']-amazon.loc[o5]['Open']+x5

    del df1,df2,df3,df4,df5

    data = [['2016', z1], ['2017', z2], ['2018', z3], ['2019',z4], ['2020',z5]] 
    df_amazon = pd.DataFrame(data, columns = ['Year', 'Return']) 
    return df_amazon

def ibm():

    ibm = yf.Ticker("IBM").history(period="5y")

    df1 = ibm.loc[(ibm.index > s1) & (ibm.index < e1)]
    df2 = ibm.loc[(ibm.index > s2) & (ibm.index < e2)]
    df3 = ibm.loc[(ibm.index > s3) & (ibm.index < e3)]
    df4 = ibm.loc[(ibm.index > s4) & (ibm.index < e4)]
    df5 = ibm.loc[(ibm.index > s5) & (ibm.index < e5)]

    x1 = df1['Dividends'].sum()
    x2 = df2['Dividends'].sum()
    x3 = df3['Dividends'].sum()
    x4 = df4['Dividends'].sum()
    x5 = df5['Dividends'].sum()

    z1 = ibm.loc[c1]['Close']-ibm.loc[o1]['Open']+x1
    z2 = ibm.loc[c2]['Close']-ibm.loc[o2]['Open']+x2
    z3 = ibm.loc[c3]['Close']-ibm.loc[o3]['Open']+x3
    z4 = ibm.loc[c4]['Close']-ibm.loc[o4]['Open']+x4
    z5 = ibm.loc[c5]['Close']-ibm.loc[o5]['Open']+x5

    del df1,df2,df3,df4,df5

    data = [['2016', z1], ['2017', z2], ['2018', z3], ['2019',z4], ['2020',z5]] 
    df_ibm = pd.DataFrame(data, columns = ['Year', 'Return']) 
    return df_ibm

def plot():
    df1 = google()
    df2 = microsoft()
    df3 = facebook()
    df4 = amazon()
    df5 = ibm()

    plt.plot(df1['Year'],df1['Return'], label = "Alphabet")
    plt.plot(df2['Year'],df2['Return'], label = "Microsoft")
    plt.plot(df3['Year'],df3['Return'], label = "Facebook")
    plt.plot(df4['Year'],df4['Return'], label = "Amazon")
    plt.plot(df5['Year'],df5['Return'], label = "IBM")

    plt.title('Return(in $) vs Year', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Return(in $)', fontsize=14)
    plt.grid(True)
    plt.legend() 
    plt.show()