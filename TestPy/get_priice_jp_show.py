import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取CSV文件
df = pd.read_csv(r"D:\Study\py_Study\TestPy\data.csv")

# 处理N/A，转换为数值
df = df.replace("N/A", pd.NA)

# 保存 code → name 映射
code2name = df.set_index("code")["name"].to_dict()

# 去掉 name 列，剩余是数值
df_numeric = df.drop(columns="name")
df_numeric.iloc[:, 1:] = df_numeric.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")

# 设置股票代码为索引
df_numeric.set_index("code", inplace=True)

# 转置
df_T = df_numeric.T
df_T.index = pd.to_datetime(df_T.index, errors="coerce")

# ✅ 选择要绘图的股票代码
#selected_codes = ["7203", "6758", "7974", "6857", "9984", "8306", "8058"]
selected_codes = ["7203", "6758", "8035","7974", "6857", "9984", "9983", "8306", "8316", "8058", "8031", "4063", "6861", "9432", "^N225"]


valid_codes = [code for code in selected_codes if code in df_T.columns]

# 绘制价格变化曲线
plt.figure(figsize=(12, 6))
for code in valid_codes:
    plt.plot(df_T.index, df_T[code], marker='o', linewidth=1.5, label=code2name.get(code, code))

plt.title("指定股票价格变化曲线", fontsize=16)
plt.xlabel("日期", fontsize=12)
plt.ylabel("价格", fontsize=12)
plt.xticks(rotation=45)
plt.legend(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.gcf().autofmt_xdate()
plt.show()
