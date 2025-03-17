from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 启动Firefox浏览器
driver = webdriver.Firefox()

# 打开前台登录页
driver.get("http://localhost/upload/user.php")

# 点击注册按钮，使用提供的XPath路径
register_button_xpath = "/html/body/div[1]/div[2]/ul/li[1]/font/a[2]"
driver.find_element(By.XPATH, register_button_xpath).click()

# 等待页面加载完毕
time.sleep(2)

# 填写注册信息
driver.find_element(By.NAME, "username").send_keys("yzx")
driver.find_element(By.NAME, "email").send_keys("20222034046@m.scnu.edu")
driver.find_element(By.NAME, "password").send_keys("20222034046")
driver.find_element(By.NAME, "confirm_password").send_keys("20222034046")
# 以下信息根据需要填写或修改
driver.find_element(By.NAME, "extend_field2").send_keys("20222034046")  # QQ号码
driver.find_element(By.NAME, "extend_field5").send_keys("13528849908")  # 手机号码
driver.find_element(By.NAME, "extend_field1").send_keys("114514@msn.com")  # MSN
driver.find_element(By.NAME, "extend_field3").send_keys("010-12345678")  # 办公电话
driver.find_element(By.NAME, "extend_field4").send_keys("021-87654321")  # 家庭电话
driver.find_element(By.NAME, "sel_question").send_keys("我最喜爱的电影？")
driver.find_element(By.NAME, "passwd_answer").send_keys("天空之城")

# 同意用户协议
# driver.find_element(By.NAME, "agreement").click()

# 提交注册信息
driver.find_element(By.NAME, "Submit").click()

# 等待一段时间以便观察或处理可能的注册后流程
time.sleep(3)

# 关闭浏览器
driver.quit()