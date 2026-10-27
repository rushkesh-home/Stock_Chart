# Stock Historical Data Visualizer

A lightweight Python script that fetches historical stock market data using `yfinance`, cleans and structures the metrics with `pandas`, and plots a High vs. Low price trend chart using `matplotlib`.

---

## Features

- **Dynamic Inputs:** Choose any ticker symbol (US or international) and specify historical lookback periods.
- **Global & Indian Exchange Support:** Supports US markets (`AAPL`, `MSFT`) and Indian exchanges via NSE/BSE tickers (`RELIANCE.NS`, `TCS.NS`, `INFY.BO`).
- **Data Structuring:** Extracts OHLCV series into clean Pandas DataFrames.
- **Visual Analytics:** Generates multi-line trend plots comparing High vs. Low trading ranges over time.
- **Automated Export:** Saves rendered charts directly as high-resolution PNG images.

---

## Prerequisites

- **Python 3.10+**
- Visual Studio Code or any terminal environment

---

## Installation

1. Clone or download this repository:
   ```bash
   git clone [https://github.com/rushkesh-home/Stock_Chart.git](https://github.com/rushkesh-home/Stock_Chart.git)
   cd stock-historical-data-visualizer
