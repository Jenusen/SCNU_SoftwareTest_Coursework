from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

# 启动Firefox浏览器
driver = webdriver.Firefox()

# 打开前台首页
driver.get("http://localhost/upload/index.php")

# 点击登录按钮，等待3秒
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
sleep(3)

# 点击左上角ECSHOP商标，等待3秒
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/a/img').click()
sleep(3)

# 点击精品推荐区里的第一个商品名称，等待3秒
driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[5]/div/div[2]/div[1]/p/a').click()
sleep(3)

# 点击“高级搜索”，等待3秒
driver.find_element(By.XPATH, '/html/body/div[4]/form/a').click()
sleep(3)

# 输入高级搜索页面里的关键字100，等待3秒
driver.find_element(By.XPATH, '//*[@id="keywords"]').send_keys('100')
sleep(3)

# 点击“立即搜索”按钮，等待3秒
driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[1]/div/div/form/table/tbody/tr[7]/td/input[2]').click()
sleep(3)

# 点击“夏新N7手机图标”，等待3秒
driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[3]/div/form/div/div/div[5]/a[1]/img').click()
sleep(3)

# 点击“查看购物车”，等待3秒
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/ul/li[2]/a[1]').click()
sleep(3)

# 关闭浏览器
driver.quit()
