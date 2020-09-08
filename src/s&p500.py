import pandas as pd 
import yfinance as yf 

first_digit_cnts = [0 for i in range(10)]
sp_companies = pd.read_csv("constituents.csv")


for sym in sp_companies["Symbol"]:
    ticker = yf.Ticker(sym)
    df = ticker.history(period="max")

    close_prices = df["Close"]
    try: today_close_price = (close_prices[-1])  # Sept. 1
    except: continue

    try: first_digit_cnts[int(str(today_close_price)[0])]+= 1
    except: continue

# [0, 166, 76, 70, 39, 40, 34, 20, 24, 30]
# [0.333, 0.152, 0.140, 0.078, 0.080, 0.068, 0.040, 0.048, 0.060]