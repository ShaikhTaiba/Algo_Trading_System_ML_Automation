import pandas as pd
import ta

def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def apply_strategy(df):
    df['RSI'] = calculate_rsi(df['Close'])
    df['20DMA'] = df['Close'].rolling(window=20).mean()
    df['50DMA'] = df['Close'].rolling(window=50).mean()
    buy_signal = (df['RSI'] < 30) & (df['20DMA'] > df['50DMA'])
    df['Signal'] = buy_signal.shift(1).fillna(False)
    return df

def backtest_strategy(df):
    df['Returns'] = df['Close'].pct_change()
    df['StrategyReturns'] = df['Signal'].shift(1) * df['Returns']
    total_return = (df['StrategyReturns'] + 1).prod() - 1
    win_trades = df[df['Signal'] & (df['Returns'] > 0)].shape[0]
    total_trades = df['Signal'].sum()
    win_ratio = win_trades / total_trades if total_trades != 0 else 0
    return total_return, win_ratio
