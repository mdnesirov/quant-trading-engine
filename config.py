"""Configuration file for the quantitative trading engine."""

import os
from pathlib import Path
from typing import List

# Base directory
BASE_DIR = Path(__file__).parent.absolute()

# Data directories
DATA_DIR = BASE_DIR / 'data'
CACHE_DIR = DATA_DIR / 'cache'
DATA_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)

# API Configuration
API_HOST = os.getenv('API_HOST', '0.0.0.0')
API_PORT = int(os.getenv('API_PORT', 8000))

# Dashboard Configuration  
DASHBOARD_PORT = int(os.getenv('DASHBOARD_PORT', 8501))

# Data Configuration
DEFAULT_TICKERS = [
    # S&P 500 Major Components
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META', 'TSLA', 'BRK-B',
    'UNH', 'JNJ', 'JPM', 'V', 'PG', 'XOM', 'HD', 'CVX', 'MA', 'BAC',
    'ABBV', 'PFE', 'COST', 'DIS', 'KO', 'AVGO', 'WMT', 'MRK', 'PEP',
    'TMO', 'CSCO', 'LLY', 'ACN', 'ABT', 'ADBE', 'MCD', 'DHR', 'NKE',
    'VZ', 'TXN', 'NEE', 'WFC', 'PM', 'ORCL', 'CRM', 'LIN', 'CMCSA',
    'BMY', 'INTC', 'AMD', 'UPS', 'RTX', 'HON', 'QCOM', 'UNP'
]

DATA_START_DATE = '2020-01-01'
CACHE_EXPIRY_DAYS = 1

# Factor Configuration
FACTOR_LOOKBACK_PERIODS = {
    'momentum': 252,  # 1 year
    'volatility': 60,  # 3 months
    'value': None,  # Current values
    'quality': None,  # Current values
    'size': None  # Current values
}

# Backtesting Configuration
BACKTEST_START_DATE = '2021-01-01'
BACKTEST_END_DATE = None  # None = today
REBALANCE_FREQUENCY = 'M'  # M=monthly, Q=quarterly, Y=yearly
TRANSACTION_COST = 0.001  # 0.1%
INITIAL_CAPITAL = 100000

# Portfolio Configuration
MAX_POSITION_SIZE = 0.10  # 10% max per position
MIN_POSITION_SIZE = 0.01  # 1% min per position
TARGET_VOLATILITY = 0.15  # 15% annual vol target
RISK_FREE_RATE = 0.03  # 3% risk-free rate

# ML Configuration
ML_TRAIN_SPLIT = 0.8
ML_RANDOM_STATE = 42
ML_FEATURES = ['momentum', 'volatility', 'value_pb', 'quality_roe', 'size']

# Dashboard Configuration
CHART_THEME = 'plotly_dark'
DEFAULT_CHART_HEIGHT = 400

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
