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

def oracle():

    oracle = yf.Ticker("ORCL").history(period="5y")

    df1 = oracle.loc[(oracle.index > s1) & (oracle.index < e1)]
    df2 = oracle.loc[(oracle.index > s2) & (oracle.index < e2)]
    df3 = oracle.loc[(oracle.index > s3) & (oracle.index < e3)]
    df4 = oracle.loc[(oracle.index > s4) & (oracle.index < e4)]
    df5 = oracle.loc[(oracle.index > s5) & (oracle.index < e5)]

    x1 = df1['Dividends'].sum()
    x2 = df2['Dividends'].sum()
    x3 = df3['Dividends'].sum()
    x4 = df4['Dividends'].sum()
    x5 = df5['Dividends'].sum()

    z1 = oracle.loc[c1]['Close']-oracle.loc[o1]['Open']+x1
    z2 = oracle.loc[c2]['Close']-oracle.loc[o2]['Open']+x2
    z3 = oracle.loc[c3]['Close']-oracle.loc[o3]['Open']+x3
    z4 = oracle.loc[c4]['Close']-oracle.loc[o4]['Open']+x4
    z5 = oracle.loc[c5]['Close']-oracle.loc[o5]['Open']+x5

    del df1,df2,df3,df4,df5

    data = [['2016', z1], ['2017', z2], ['2018', z3], ['2019',z4], ['2020',z5]] 
    df_oracle = pd.DataFrame(data, columns = ['Year', 'Return']) 
    return df_oracle

def tcs():

    tcs = yf.Ticker("TCS.NS").history(period="5y")

    df1 = tcs.loc[(tcs.index > s1) & (tcs.index < e1)]
    df2 = tcs.loc[(tcs.index > s2) & (tcs.index < e2)]
    df3 = tcs.loc[(tcs.index > s3) & (tcs.index < e3)]
    df4 = tcs.loc[(tcs.index > s4) & (tcs.index < e4)]
    df5 = tcs.loc[(tcs.index > s5) & (tcs.index < e5)]

    x1 = df1['Dividends'].sum()
    x2 = df2['Dividends'].sum()
    x3 = df3['Dividends'].sum()
    x4 = df4['Dividends'].sum()
    x5 = df5['Dividends'].sum()

    z1 = tcs.loc[c1]['Close']-tcs.loc[o1]['Open']+x1
    z2 = tcs.loc[c2]['Close']-tcs.loc[o2]['Open']+x2
    z3 = tcs.loc[c3]['Close']-tcs.loc[o3]['Open']+x3
    z4 = tcs.loc[c4]['Close']-tcs.loc[o4]['Open']+x4
    z5 = tcs.loc[c5]['Close']-tcs.loc[o5]['Open']+x5

    del df1,df2,df3,df4,df5

    data = [['2016', z1], ['2017', z2], ['2018', z3], ['2019',z4], ['2020',z5]] 
    df_tcs = pd.DataFrame(data, columns = ['Year', 'Return']) 
    return df_tcs

def infosys():

    infosys = yf.Ticker("INFY.NS").history(period="5y")

    df1 = infosys.loc[(infosys.index > s1) & (infosys.index < e1)]
    df2 = infosys.loc[(infosys.index > s2) & (infosys.index < e2)]
    df3 = infosys.loc[(infosys.index > s3) & (infosys.index < e3)]
    df4 = infosys.loc[(infosys.index > s4) & (infosys.index < e4)]
    df5 = infosys.loc[(infosys.index > s5) & (infosys.index < e5)]

    x1 = df1['Dividends'].sum()
    x2 = df2['Dividends'].sum()
    x3 = df3['Dividends'].sum()
    x4 = df4['Dividends'].sum()
    x5 = df5['Dividends'].sum()

    z1 = infosys.loc[c1]['Close']-infosys.loc[o1]['Open']+x1
    z2 = infosys.loc[c2]['Close']-infosys.loc[o2]['Open']+x2
    z3 = infosys.loc[c3]['Close']-infosys.loc[o3]['Open']+x3
    z4 = infosys.loc[c4]['Close']-infosys.loc[o4]['Open']+x4
    z5 = infosys.loc[c5]['Close']-infosys.loc[o5]['Open']+x5

    del df1,df2,df3,df4,df5

    data = [['2016', z1], ['2017', z2], ['2018', z3], ['2019',z4], ['2020',z5]] 
    df_infosys = pd.DataFrame(data, columns = ['Year', 'Return']) 
    return df_infosys

def plot():
    df1 = google()
    df2 = microsoft()
    df3 = oracle()
    df4 = tcs()
    df5 = infosys()

    plt.plot(df1['Year'],df1['Return'], label = "Google")
    plt.plot(df2['Year'],df2['Return'], label = "Microsoft")
    plt.plot(df3['Year'],df3['Return'], label = "Oracle")
    plt.plot(df4['Year'],df4['Return'], label = "TCS")
    plt.plot(df5['Year'],df5['Return'], label = "Infosys")

    plt.title('Return(in $) vs Year', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Return(in $)', fontsize=14)
    plt.grid(True)
    plt.legend() 
    plt.show()