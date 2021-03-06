import datetime as dt
import pandas as pd
import os
import calc
import term


def main():
    pd.set_option('precision', 3)
    today = dt.datetime.today()
    years = today - dt.timedelta(days=365*3) 
    try:
        csv = pd.read_csv(os.path.abspath("stocks.csv"))
    except Exception as e:
        print(term.col.WARNING, "Execution Error: %s" % e, term.colENDC)
    data = calc.grab_data(csv, years, today)
    #data = data[data['Dip?']=='Ye']
    term.terminal(data, data.index)

if __name__=="__main__":
    main()
