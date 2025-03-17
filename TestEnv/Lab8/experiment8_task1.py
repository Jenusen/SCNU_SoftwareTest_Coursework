from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# 步骤1: 打开ECSHOP前台首页
driver = webdriver.Firefox()
driver.get("http://localhost/upload/index.php")
sleep(2)  # 给页面加载预留足够的时间

# 步骤2: 定位到登录按钮，并单击
login_button_xpath = '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img'
login_button = driver.find_element(By.XPATH, login_button_xpath)
ActionChains(driver).click(login_button).perform()
sleep(2)  # 单击后等待，模拟用户的延迟

# 步骤3-4: 鼠标移动到用户名文本框元素，单击并输入"vip"
username_input_css = '.usBox_1 > form:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)'
username_input = driver.find_element(By.CSS_SELECTOR, username_input_css)
ActionChains(driver).move_to_element(username_input).click().send_keys("vip").perform()
sleep(2)  # 输入用户名后的延迟

# 步骤5-9: 输入密码"vip"并模拟更多操作
ActionChains(driver).send_keys(Keys.TAB).pause(2).send_keys("vip").pause(2).send_keys(Keys.TAB).pause(2).perform()
sleep(2)  # 模拟在不同输入字段间的延迟

# 步骤10: 按下回车键进行登录
ActionChains(driver).send_keys(Keys.ENTER).perform()
sleep(5)  # 登录后等待，观察页面反应

# 步骤11: 关闭浏览器
driver.close()
