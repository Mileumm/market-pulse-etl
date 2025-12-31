"""
Nom du script : market-pulse-etl.py
Description    : A production-ready ETL pipeline
Auteur         : Theo
Date           : 2025-12-08
"""


# ---------------------------
#1. Imports
#----------------------------

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import logging
from logging.handlers import RotatingFileHandler

#----------------------------
#2. Constantes
#----------------------------

logger = logging.getLogger('my_logger')

#----------------------------
#3. Classes
#----------------------------

#----------------------------
#4. Functions
#----------------------------
def get_market_data(ticker_symbol, days_back=30):

    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
    
    data = yf.download(ticker_symbol, start=start_date, end=end_date, progress=False)
    
    if data.empty:
        print(f"Warning: No data found for {ticker_symbol}")
        return None
        
    return data

def handle_weekends(df):
    # Ensure the index is a datetime type
    df.index = pd.to_datetime(df.index)
    
    # 1. Resample to include ALL days (fills Saturday/Sunday with NaN)
    df_resampled = df.resample('D').asfreq()
    
    # 2. Forward fill (ffill) empty values from the last known price (Friday)
    df_clean = df_resampled.ffill()
    
    return df_clean
#----------------------------
#5. Main
#----------------------------

def main():
    ticker = "AAPL" # Apple
    raw_df = get_market_data(ticker)
    
    if raw_df is not None:
        raw_df = handle_weekends(raw_df)
        print(raw_df.head())
        raw_df.to_csv(f"{ticker}_raw.csv")
        

#----------------------------
#6. Door
#----------------------------

if __name__ == "__main__":
    main()
