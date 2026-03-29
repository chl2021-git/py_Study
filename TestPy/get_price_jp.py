import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_stock_prices_by_date(stock_codes, date_list):
    """
    根据 date_list 的每个日期，分别下载并获取收盘价。
    每次只请求一个日期的前后范围，避免一次性下载过多数据。
    """
    # 区分日本股票和指数
    jp_stocks = [code for code in stock_codes if not code.startswith('^')]
    indices = [code for code in stock_codes if code.startswith('^')]

    # 为日本股票添加 '.T' 后缀
    all_tickers = [f"{code}.T" for code in jp_stocks] + indices

    records = []

    for date_str in date_list:
        date_obj = pd.to_datetime(date_str)

        try:
            # 下载指定日期前后 3 天的数据（避免停牌或周末无数据）
            data = yf.download(
                all_tickers,
                start=date_obj - timedelta(days=3),
                end=date_obj + timedelta(days=3),
                progress=False,
                auto_adjust=True
            )

            if data.empty:
                record = pd.Series([None] * len(stock_codes), index=stock_codes, name=date_str)
                records.append(record)
                continue

            close_prices = data['Close']

            # 统一列名，去掉 '.T'
            close_prices.columns = [col.replace('.T', '') for col in close_prices.columns]

            # 找到最接近指定日期的交易日（不晚于指定日期）
            actual_date = close_prices.index.asof(date_obj)

            if pd.notna(actual_date) and actual_date <= date_obj:
                record = close_prices.loc[actual_date].reindex(stock_codes)
                record.name = date_str
                records.append(record)
            else:
                record = pd.Series([None] * len(stock_codes), index=stock_codes, name=date_str)
                records.append(record)

        except Exception as e:
            print(f"下载 {date_str} 数据时发生错误: {e}")
            record = pd.Series([None] * len(stock_codes), index=stock_codes, name=date_str)
            records.append(record)

    df = pd.DataFrame(records)
    return df.applymap(lambda x: int(x) if pd.notna(x) else None)


# --- 主程序 ---
if __name__ == "__main__":
    stock_codes = [
        '7203', '6758', '8035', '7974', '6857', '9984', '9983',
        '8306', '8316', '8058', '8031', '4063', '6861', '9432',
        '^N225',  # 日经225指数
        '1330', '1489', '2569', '1545', '1660', '314A','1540',
        "^GSPC", "^IXIC"
    ]
    
    date_list = ['2025-01-27','2026-01-05', '2026-01-26']

    prices_df = get_stock_prices_by_date(stock_codes, date_list)

    if not prices_df.empty:
        print("查询日期收盘价 (整数，未获取显示 N/A):\n")
        formatted_df = prices_df.applymap(lambda x: f"{int(x):,}" if pd.notna(x) else "N/A")
        print(formatted_df.T)

        # 保存到 Excel
        file_name = 'stock_prices.xlsx'
        prices_df.T.to_excel(file_name, sheet_name='Close_Prices', index=True, header=True)
    else:
        print("未能获取到任何价格数据。")
