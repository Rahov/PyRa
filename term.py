import pandas as pd


class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def terminal(_stocks, _csv):
    print(col.UNDERLINE+"{:<8s}|  {:<8s}|  {:<8s}|  {:<6s}|  {:<6s}|  {:<8s}|  {:<6s}|  {:<8s}|".format("Symbol", _stocks.columns[2], _stocks.columns[0], _stocks.columns[6], _stocks.columns[4], _stocks.columns[1], _stocks.columns[3], _stocks.columns[5]), col.ENDC)
    for i in range(0, len(_csv)):
        print(col.BOLD+"{:<8}\033[0m|  ".format(_csv[i]), end="")
        print("{:<8.2f}|  ".format(_stocks["Close"][i]), end="")
        if _stocks['20-MA'][i] > _stocks['Close'][i]:
            print(col.OKGREEN+"{:<8.2f}\033[0m|  ".format(_stocks["20-MA"][i]), end="")
        else:
            print("{:<8.2f}|  ".format(_stocks["20-MA"][i]), end="")
        if _stocks['RSI'][i] < 35:
            print(col.OKGREEN+"{:<6.1f}\033[0m|  ".format(_stocks["RSI"][i]), end="")
        else:
            print("{:<6.1f}|  ".format(_stocks["RSI"][i]), end="")
        if _stocks['MACD'][i] < 0.1:
            print(col.OKGREEN+"{:<6.1f}\033[0m|  ".format(_stocks["MACD"][i]), end="")
        else:
            print("{:<6.1f}|  ".format(_stocks["MACD"][i]), end="")
        if _stocks['52-High'][i]*0.9 > _stocks['Close'][i]:
            print(col.OKGREEN+"{:<8.1f}\033[0m|  ".format(_stocks["52-High"][i]), end="")
        else:
            print("{:<8.1f}|  ".format(_stocks["52-High"][i]), end="")
        if _stocks['Dip?'][i] == 'Ye':
            print(col.OKGREEN+"{:<6s}\033[0m|  ".format(_stocks["Dip?"][i]), end="")
        else:
            print(col.FAIL+"{:<6s}\033[0m|  ".format(_stocks["Dip?"][i]), end="")
        print("{:<8.2f}|  ".format(_stocks["R-rate"][i]))
    return
