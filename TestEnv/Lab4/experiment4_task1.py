from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 启动火狐浏览器
driver = webdriver.Firefox()

# 打开前台首页
driver.get("http://localhost/upload/index.php")

# 点击“留言板”按钮，等待3秒
driver.find_element(By.CSS_SELECTOR, "#mainNav > a:nth-child(10)").click()
sleep(3)

# 在电子邮件地址文本框里输入vip@163.com
driver.find_element(By.CSS_SELECTOR,
                    ".AreaR > div:nth-child(6) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > "
                    "table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child("
                    "1)").send_keys(
    "vip@163.com")

# 判断“询问”按钮是否选中，若否，选中“询问”按钮，等待2秒
inquiry_button = driver.find_element(By.CSS_SELECTOR, ".AreaR > div:nth-child(6) > div:nth-child(1) > div:nth-child("
                                                      "2) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child("
                                                      "1) > tr:nth-child(3) > td:nth-child(2) > input:nth-child(3)")
if not inquiry_button.is_selected():
    inquiry_button.click()
sleep(2)

# 在主题文本框中输入“维修”
driver.find_element(By.CSS_SELECTOR,
                    ".AreaR > div:nth-child(6) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > "
                    "table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > input:nth-child("
                    "1)").send_keys(
    "维修")

# 在留言内容文本域输入“手机坏了怎么处理？”
driver.find_element(By.CSS_SELECTOR,
                    ".AreaR > div:nth-child(6) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > "
                    "table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > "
                    "textarea:nth-child(1)").send_keys(
    "手机坏了怎么处理？")

# 点击我要留言按钮，等待1秒
driver.find_element(By.CSS_SELECTOR, ".bnt_blue_1").click()
sleep(1)

# 关闭浏览器
driver.quit()
