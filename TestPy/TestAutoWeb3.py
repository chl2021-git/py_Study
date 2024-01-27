import requests
from bs4 import BeautifulSoup

def get_webpage_content(url):
    try:
        # 发送GET请求获取网页内容
        response = requests.get(url)
        response.encoding = 'utf-8' 
        
        # 检查请求是否成功
        response.raise_for_status()
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 这里可以根据具体的网页结构提取你需要的内容
        # 以下是一个简单的示例，提取网页标题
        
        title = soup.title.text
        print(f"网页标题: {title}")
        contents = soup.find('div', class_="panel-body")
        #print(contents.get_text())
        
        #f = open('D:\\Study\\py_Study\\TestPy\\test_f\\' + url[33:] , mode='w',encoding='UTF-8') 
        f = open('D:\\Study\\py_Study\\TestPy\\test_f\\all.txt' , mode='a+',encoding='UTF-8') 
        f.write(contents.get_text())
        f.close

        # 如果需要提取其他内容，可以继续在这里添加代码
        
    except requests.exceptions.RequestException as e:
        print(f"发生错误: {e}")
#
if __name__ == "__main__":
    
    for num in range(116964,117082): 
        # 你的目标网页URL
        target_url = "https://www.luoxia123.com/feidu/%d.html"  % num
        
        # 调用函数获取网页内容
        get_webpage_content(target_url)
