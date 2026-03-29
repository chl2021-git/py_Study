import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

# iFreeNEXT FANG+ Index 在乐天证券的详情页 ID
RAKUTEN_FUND_ID = "JP90C000FZD4"
RAKUTEN_URL = f"https://www.rakuten-sec.co.jp/web/fund/detail/?ID={RAKUTEN_FUND_ID}"
FUND_NAME = "Daiwa iFreeNEXT FANG+ Index"

def get_rakuten_fund_nav(fund_id, date_str):
    """
    通过网页抓取乐天证券页面获取基金净值。
    注意：此方法只能获取网页上显示的最新数据，通常是 T-1 日期的数据。
    无法像下载历史 CSV 那样精确指定历史日期。
    
    Args:
        fund_id (str): 乐天证券的基金ID (JP90C...)。
        date_str (str): 仅用于输出显示，实际抓取的是页面上的“最新”净值。

    Returns:
        str: 提取到的最新净值和其对应的日期。
    """
    
    try:
        print(f"正在尝试从乐天证券获取 {FUND_NAME} ({fund_id}) 的最新净值...")
        
        # 模拟浏览器请求
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(RAKUTEN_URL, headers=headers)
        response.encoding = 'utf-8'

        if response.status_code != 200:
            return f"错误：无法访问乐天证券页面。HTTP 状态码: {response.status_code}"
        
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # --- 查找净值 (基準価額) ---
        # 乐天证券的净值通常在一个特定的 div 结构中
        # 假设净值在一个 class 为 "f-detail-data-val-big" 的 span/div 中
        nav_element = soup.find('span', class_='f-detail-data-val-big')
        
        if not nav_element:
            # 如果找不到，尝试另一个可能的结构 (网站改版或结构不同)
            # 这需要根据目标网站的最新HTML结构进行调整
            nav_element = soup.find('div', class_='f-detail-data-val')
            if not nav_element:
                return f"错误：无法在乐天证券页面上定位到净值数据 (f-detail-data-val-big 或 f-detail-data-val)。网站结构可能已改变。"
        
        # 清理净值数据 (移除日元符号、逗号等)
        nav_raw = nav_element.text.strip()
        nav_price = nav_raw.replace('円', '').replace(',', '')
        
        # --- 查找净值对应的日期 ---
        # 假设日期在一个紧随净值或附近的元素中，我们寻找包含日期信息的文本
        
        # 尝试寻找包含 "(MM/DD)" 格式日期的元素
        date_text_element = soup.find('p', class_='f-detail-data-date')

        if date_text_element:
             date_text = date_text_element.text.strip()
             # 提取括号内的 MM/DD 格式日期
             date_match = pd.Series(date_text).str.extract(r'\((\d{1,2}/\d{1,2})\)')[0].iloc[0]
             
             if pd.isna(date_match):
                 # 如果未能匹配，则使用当前年份
                 current_year = datetime.now().year
                 nav_date = f"无法确定 (页面日期格式不明确)"
             else:
                 # 将 MM/DD 格式和当前年份组合，并格式化为 YYYY-MM-DD
                 current_year = datetime.now().year
                 nav_date_obj = datetime.strptime(f"{current_year}/{date_match}", '%Y/%m/%d')
                 nav_date = nav_date_obj.strftime('%Y-%m-%d')
        else:
             nav_date = "无法确定 (页面日期元素f-detail-data-date缺失)"


        # 检查是否为数字，如果是，则格式化
        try:
            nav_price_formatted = float(nav_price)
            price_output = f"{nav_price_formatted:,.0f} 日元"
        except ValueError:
            price_output = nav_price
            
        return (
            f"基金名称: {FUND_NAME}\n"
            f"数据来源: 乐天证券 (页面抓取)\n"
            f"最新净值（基準価額）公布日期: {nav_date}\n"
            f"最新净值: {price_output}"
        )

    except Exception as e:
        return f"查询时发生错误：{type(e).__name__}: {e}"

# --- 用户输入和调用 ---
if __name__ == "__main__":
    
    # 基金代码已固定为 RAKUTEN_FUND_ID
    # 由于是网页抓取，我们忽略用户输入的日期，只获取页面上的“最新”数据
    
    print("注意：通过网页抓取只能获取页面上显示的“最新”净值（通常是T-1日数据）。")
    print("无法精确获取指定历史日期的数据。")
    
    # 模拟输入，但实际未被函数使用
    # 我们仍然需要一个 date_str 参数来保持函数签名一致，但在此例中它不再影响结果
    dummy_date_input = datetime.now().strftime('%Y-%m-%d')

    result = get_rakuten_fund_nav(RAKUTEN_FUND_ID, dummy_date_input)
    print("\n--- 结果 ---")
    print(result)