from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 启动火狐浏览器
driver = webdriver.Firefox()

# 隐式等待3秒
driver.implicitly_wait(3)

# 打开前台首页
driver.get("http://localhost/upload/index.php")

# 在首页的文本框中输入“30”
input_element = driver.find_element(By.NAME, "keywords")
input_element.send_keys("30")

# 点击搜索按钮
search_button = driver.find_element(By.NAME, "imageField")
search_button.click()

# 等待5秒
sleep(5)

# 关闭浏览器
driver.quit()
