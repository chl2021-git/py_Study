from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def get_webpage_content_with_selenium(url):
    try:
        # 配置ChromeDriver的路径
        driver_path = 'D:\\Study\\chromedriver\\chromedriver.exe'

        # 创建 Chrome 浏览器驱动对象
        driver = webdriver.Chrome(driver_path)

        # 打开网页
        driver.get(url)

        # 等待一段时间，以确保页面加载完成（根据需要调整等待时间）
        driver.implicitly_wait(10)

        # 使用Selenium定位元素，这里以提取网页标题为例
        title_element = driver.find_element(By.TAG_NAME, 'title')
        title = title_element.text
        print(f"网页标题: {title}")

        # 如果需要提取其他内容，可以继续在这里添加代码

    finally:
        # 关闭浏览器
        driver.quit()

if __name__ == "__main__":
    # 你的目标网页URL
    target_url = "https://www.luoxia123.com/feidu/116965.html"

    # 调用函数获取网页内容
    get_webpage_content_with_selenium(target_url)
