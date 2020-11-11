import datetime as dt
import pandas as pd
import os
import calc
import term


def main():
    pd.set_option('precision', 3)
    today = dt.datetime.today()
    YTD = today - dt.timedelta(days=365) 
    try:
        csv = pd.read_csv(os.path.abspath("stocks.csv"))
    except Exception as e:
        print(term.col.WARNING, "Execution Error: %s" % e, term.colENDC)
    data = calc.grab_data(csv[0:2], '2018', '2019') 
    term.terminal(data, data.index)

if __name__=="__main__":
    main()
