import yfinance as yf

def fetch_stock_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end, interval="1d")
    df.dropna(inplace=True)
    return df