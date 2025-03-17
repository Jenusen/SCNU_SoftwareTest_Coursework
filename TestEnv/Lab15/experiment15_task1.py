from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 设置Firefox驱动
driver = webdriver.Firefox()

# 打开ECShop前台登录页
driver.get("http://localhost/upload/user.php")

# 输入用户名
username = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/form/table/tbody/tr[1]/td[2]/input")
username.send_keys("vip")

# 输入密码
password = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/form/table/tbody/tr[2]/td[2]/input")
password.send_keys("vip")

# 点击“立即登陆”
login_button = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/form/table/tbody/tr[3]/td[2]/input[3]")
login_button.click()

# 等待5秒
time.sleep(5)

# 点击上方“用户中心”
user_center = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/font/font/a[1]")
user_center.click()

# 等待3秒
time.sleep(3)

# 点击左侧“我的留言”
my_message = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div/div/div/div/a[6]")
my_message.click()

# 等待3秒
time.sleep(3)

# 输入主题
subject = driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/div/div/form/table/tbody/tr[2]/td[2]/input")
subject.send_keys("hello")

# 输入留言内容
message_content = driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/div/div/form/table/tbody/tr[3]/td[2]/textarea")
message_content.send_keys("welcome to this world!")

# 选择文件
file_upload = driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/div/div/form/table/tbody/tr[4]/td[2]/input")
file_upload.send_keys("c:\\temp\\777.txt")
# 点击“提交”
submit_button = driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/div/div/form/table/tbody/tr[5]/td[2]/input[2]")
submit_button.click()

# 关闭浏览器
driver.quit()
