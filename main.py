from config import NIFTY_STOCKS, START_DATE, END_DATE, SHEET_NAME, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from utils import fetch_stock_data
from strategy import apply_strategy, backtest_strategy
from ml_model import train_model
from sheets_logger import connect_sheet, log_to_sheet
from alerts import send_telegram_alert

def run():
    sheet = connect_sheet(SHEET_NAME)

    for stock in NIFTY_STOCKS:
        df = fetch_stock_data(stock, START_DATE, END_DATE)
        df = apply_strategy(df)

        signals = df[df['Signal']]
        print(f"{stock} — Buy signals found: {len(signals)}")
        trades = [
            [str(stock), str(date.strftime('%Y-%m-%d')), float(row['Close'])]
            for date, row in signals.iterrows()
        ]

        if trades:
            log_to_sheet(sheet, "Trade Log", trades)
            msg = f"Buy Signal for {stock} on {trades[-1][1]} at Rs.{trades[-1][2]:.2f}"
            send_telegram_alert(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, msg)

        total_return, win_ratio = backtest_strategy(df)
        summary = [[stock, f"{total_return:.2%}", f"{win_ratio:.2%}"]]
        log_to_sheet(sheet, "P&L Summary", summary)

        model, acc = train_model(df)
        log_to_sheet(sheet, "ML Accuracy", [[stock, f"{acc:.2%}"]])
        print(f"{stock} ML Accuracy: {acc:.2%}")

if __name__ == "__main__":
    run()