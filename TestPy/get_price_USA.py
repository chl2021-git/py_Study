import yfinance as yf
import pandas as pd
import numpy as np

def get_prices_on_dates(symbols, dates):
    """
    获取多个股票/指数在指定日期的收盘价。
    返回 DataFrame，行是指定日期，列为股票代码（顺序固定为 symbols）。
    """
    records = []

    for d in dates:
        try:
            d_dt = pd.to_datetime(d)
            start = d_dt - pd.Timedelta(days=5)
            end = d_dt + pd.Timedelta(days=5)

            data = yf.download(symbols, start=start, end=end, auto_adjust=False, progress=False)
            close_data = data["Close"]

            # 单个 symbol 情况
            if isinstance(close_data, pd.Series):
                close_data = close_data.to_frame(symbols[0])

            if not close_data.empty:
                # 找离请求日最近的交易日
                actual_date = close_data.index[np.argmin(np.abs(close_data.index - d_dt))]
                prices = {s: close_data.loc[actual_date][s] if s in close_data.columns else None for s in symbols}
            else:
                prices = {s: None for s in symbols}

            record = {"RequestedDate": d}
            record.update(prices)
            records.append(record)

        except Exception as e:
            print(f"Error fetching {d}: {e}")
            record = {"RequestedDate": d}
            for s in symbols:
                record[s] = None
            records.append(record)

    df = pd.DataFrame(records).set_index("RequestedDate")
    df = df[symbols]  # 保证顺序
    return df.round(2)


# 股票和指数代码
symbols = [
    "NVDA", "MSFT", "GOOG", "AMZN", "META", "AAPL",
    "JPM", "BAC", "V", "MA", "JNJ", "LLY", "UNH",
    "BA", "GE", "WMT", "KO", "PEP", "TSLA",
    "^GSPC", "^IXIC"
]


# 指定日期
dates = ["2025-01-06", "2024-10-10", "2025-10-10"]

df = get_prices_on_dates(symbols, dates)

# 打印表格（转置让日期显示在上方，股票代码在行上）
print(df.T)
