import pandas as pd
import numpy as np
import requests
import re
import time
import datetime

def CHNtime2strtime(CHNtime):

    CHNtime_list = re.findall(r'[\u4e00-\u9fa5]+',CHNtime)

    for i in CHNtime_list:

        if i != '日':

            CHNtime = CHNtime.replace(str(i),'-')

        else:

            CHNtime = CHNtime.replace(str(i),'')

    return CHNtime

def diff_days(str_time):   

    date_time = datetime.datetime.strptime(str_time,'%Y-%m-%d')

    now_time = datetime.datetime.now()

    diff_time = now_time - date_time

    days = diff_time.days

    return days

t = [] # 时间

dollar = [] # 美元


i = 8121 # 本文从id=5001（即2019-5-6）开始爬取

while True:  # 设置死循环


    i += 1    # 循环一次，id+1

# 请求头

    #headers = {
    #    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    #}

    headers= {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }

# 网址

    url = 'https://chl.cn/?id={}'.format(str(i))

# 请求响应

    r = requests.get(url,headers=headers)

    r.encoding = 'utf-8'

    s = r.text

    try:  #设置抛出异常，因为有些id，如id=7001，网页就不存在


        rate_list = re.findall(r'<td><a href=".*?">(.*?)</a>/人民币</td><td>(.*?)</td>',s)

        tt = re.findall(r'<h1>(.*?)汇率，外汇牌价</h1>',s)[0] #日期
        #<h1>2019年5月8日汇率，外汇牌价</h1>

        strtime = CHNtime2strtime(tt) #中文时间转字符串时间


        t.append(datetime.datetime.strptime(strtime,'%Y-%m-%d'))

        dollar.append(rate_list[0][1]) #美元


        days = diff_days(strtime) # 计算天数差

        print(tt,'爬取成功！')

        print('当天距离现在相差：',days,'天')

        if days == 0: #死循环终止条件：天数差为0时，即代表爬取到今天

            break


    except:

# 如果爬取的url不存在，那么时间与汇率就用控制代替

        t.append(np.nan)

        dollar.append(np.nan)

        print('id = ',i,'',np.nan)

        break

    time.sleep(0.2) #为了防止爬取的速度过快，设置睡眠时间为0.2s


df = pd.DataFrame() # 生产一个DataFrame用来存放数据

df['time'] = t

df['人民币兑美元汇率'] = dollar

df.dropna(inplace=True) # 将缺失值删去

df.to_excel('历史人民币兑美元汇率.xlsx',index=False) #在目前文件夹上生成excel文件

print('历史人民币兑美元汇率.xlsx 文件生成成功！')