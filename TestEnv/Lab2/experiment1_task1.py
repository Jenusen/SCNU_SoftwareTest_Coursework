from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# 启动Firefox浏览器
driver = webdriver.Firefox()

# 隐式等待，提高稳定性
driver.implicitly_wait(16)

# 浏览器窗口最大化
driver.maximize_window()

# 打开前台登录页
driver.get('http://localhost/upload/user.php')

# 输入用户名
driver.find_element(By.NAME, 'username').send_keys('vip')

# 输入密码
driver.find_element(By.NAME, 'password').send_keys('vip')

# 点击立即登录
driver.find_element(By.NAME, 'submit').click()

# 等待1秒，以便登录操作完成
sleep(1)

# 点击用户中心
driver.find_element(By.LINK_TEXT, '用户中心').click()

# 等待2秒，页面加载
sleep(2)

# 点击左侧的“用户信息”
driver.find_element(By.LINK_TEXT, '用户信息').click()

# 等待5秒，查看用户信息或进行其他操作
sleep(5)

# 关闭浏览器
driver.quit()
