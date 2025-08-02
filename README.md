# Algo-Trading System with ML Automation

This project is a Python-based mini algo-trading prototype that:
- Connects to stock data using Yahoo Finance API
- Implements a simple RSI + Moving Average Crossover strategy
- Logs trade signals and backtesting results to Google Sheets
- Uses a Decision Tree model to predict next-day price movement 
- Sends Telegram alerts for new trade signals

## Features Implemented
### 1. Data Ingestion
- Fetches 6 months of daily stock data for 3 NIFTY 50 stocks from Yahoo Finance.
### 2. Trading Strategy
- Buy Signal when:
   - RSI < 30
   - 20-DMA > 50-DMA
- Backtested for total returns and win ratio.
### 3. ML Automation
- Decision Tree classifier to predict next-day stock movement.
- Uses RSI, 20DMA, 50DMA as features.
- Logs model accuracy.
### 4. Google Sheets Automation
- Logs all buy signals into "Trade Log" tab
- Logs total return and win ratio into "P&L Summary"
- Logs model accuracy into "ML Accuracy"
### 5. Automation + Telegram Alerts
- Sends buy alerts via Telegram with price and stock info.

## Setup Instructions

### 1. Install Dependencies
Use the following command to install all required libraries:
```bash
pip install yfinance ta pandas gspread oauth2client scikit-learn requests
```

### 2. Google Sheets Setup
- Go to https://console.cloud.google.com/
- Create a new project and enable Google Sheets API and Google Drive API
- Create a Service Account under “Credentials”
- Download the JSON credentials file (creds.json)
- Share your target Google Sheet with the service account email from the JSON file
- Place creds.json inside a folder named sheets/

### 3. Telegram Bot Setup (Optional Bonus)
- Open Telegram and search for @BotFather
- Run /newbot and follow the steps to create a bot
- Copy the token provided by BotFather
- Search for @userinfobot on Telegram and start it to get your chat ID
- Add the token and chat ID to your config.py file:
```bash
TELEGRAM_BOT_TOKEN = "your_token"
TELEGRAM_CHAT_ID = "your_chat_id"
```

## Run the Project
```bash
python main.py
```

## Sample Output (on console)
```bash
TCS.NS ML Accuracy: 72.00%
RELIANCE.NS ML Accuracy: 69.38%
Buy Signal for INFY.NS on 2024-05-15 at Rs.1401.32
```

## Author
TAIBA SHAIKH
taibashaikh025@gmail.com
