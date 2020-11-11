import pandas_datareader.data as web
import pandas as pd
import numpy  as np
import term
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    return

def macd(df):
    df['EMA12'] = df['Close'].ewm(span=12, adjust=False).mean()
    df['EMA26'] = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = df['EMA12'] - df['EMA26']
    df['EMA9'] = df['MACD'].ewm(span=9, adjust=False).mean()
    return df['MACD'].iloc[-1]

def rsi(df):
    delta = df['Close'].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    avgUp = up.ewm(com=13,min_periods=14).mean()
    avgDown= abs(down.ewm(com=13,min_periods=14).mean())
    df['RSI'] = 100 - (100/ (1+avgUp/avgDown))
    return df['RSI'].iloc[-1]

def boll(df):
    df['20-MA'] = df['Close'].rolling(window=20).mean()
    df['SD'] = df['Close'].rolling(window=20).std()
    df['B-Up'] = df['20-MA'] + 2*df['SD']
    df['B-Lo'] = df['20-MA'] - 2*df['SD']
    return df['20-MA'].iloc[-1]

def _52h(df):
    df['52-High'] = max(df['Close'])
    return df['52-High'].iloc[-1]

def r_rate(df, _year, _day):
    _arr = np.array([])
    for i in range(0, _day.year - _year.year):
        try:
            _arr = np.append(_arr, (df[str(_day.year - i)].iloc[-1] / df[str(_day.year - i)].iloc[0] - 1)*100)
        except: 
            pass
    return np.average(_arr)

def dip(df):
    if ( df['MACD'] < 0.1 and df['RSI'] < 35 and df['20-MA'] > df['Close'] ):
        return 'Ye'
    else: 
        return 'No'

def grab_data(_csv, start_year, end_year):
    print(term.col.UNDERLINE + "Grabbing Data" + term.col.ENDC)
    d = {}
    _stocks = pd.DataFrame(d)
    for i in range(0, len(_csv['Symbol'])):
        try:
            dff = web.DataReader(_csv['Symbol'][i], 'yahoo', start_year, end_year)
            print("[%d]" % i + " Grabbing Stock: " + term.col.BOLD + _csv['Symbol'][i]+ term.col.ENDC)
        except Exception as e:
            print(term.col.WARNING + "[%d]" % i + "Error at Stock: " + term.col.BOLD +_csv['Symbol'][i] + term.col.ENDC)
            continue
        _stocks = _stocks.append({"Symbol": _csv['Symbol'][i], "Close": dff['Close'].iloc[-1], "MACD": macd(dff), "20-MA": boll(dff), "RSI": rsi(dff), "52-High": _52h(dff), "R-rate": r_rate(dff['Close'], start_year, end_year), "Dip?": dip(dff.iloc[-1])}, ignore_index=True)
    _stocks = _stocks.set_index('Symbol')
    clear()
    return _stocks
