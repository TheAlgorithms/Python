import panda as pd
import yfinance as yf
import datetime
from date time import date,timedelta
import plotly.graph_objects as go
import plotly.express as px
today  = date.today()
d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=365)
d2 = d2.strftime("%Y-%m-%d")
start_date= d2
data = yf.download('GOOG' ,
                   start = start_date,
                   end = end_date ,
                   progress = False)
data["Date"] = data.index
data = data[["Date","Open","High","Low",
             "Close","Adj Close" , "volume"]]
data.reset_index(drop=True,inplace=True)
print(data.head())

figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["open"],high=data["High"],
                                        low = data["low"],close=data["close"])])

figure.update_layout(title = "Google stock price analysis", xaxis_rangeslider_visible=False)
figure.show()
                 
                   

                    
