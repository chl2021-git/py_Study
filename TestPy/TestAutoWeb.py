from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 设置 Chrome 浏览器驱动的路径
driver_path = 'D:\\Study\\chromedriver\\chromedriver.exe'

# 创建 Chrome 浏览器驱动对象
driver = webdriver.Chrome(driver_path)

# 打开谷歌网站
driver.get('https://www.google.com')

# 找到搜索框，并输入指定的关键词
#search_box = driver.find_element(By.ID, "input")
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Python 自动化')

# 模拟键盘按键，按下回车键
search_box.send_keys(Keys.RETURN)

# 等待页面加载完成
driver.implicitly_wait(10)

# 打印搜索结果的标题
#result_links = driver.find_elements_by_css_selector('h3')
result_links = driver.find_elements(By.CSS_SELECTOR,'h3')
for link in result_links:
    print(link.text)

# 关闭浏览器
driver.quit()
