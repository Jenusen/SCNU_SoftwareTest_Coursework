from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 启动驱动程序并打开ECSHOP前台首页
driver = webdriver.Firefox()
driver.get('http://localhost/upload/index.php')

wait = WebDriverWait(driver, 10)

# 2. 点击“搜索”按钮，触发 alert 弹窗
driver.find_element(By.XPATH, '/html/body/div[4]/form/input[2]').click()

# 3. 等待并切换到 alert，获取文本并打印
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)

# 4. 点击“确定”按钮
alert.accept()

# 5. 输入商品编号 806 并点击“搜索”
driver.find_element(By.XPATH, '/html/body/div[4]/form/input[1]').send_keys('806')
driver.find_element(By.XPATH, '/html/body/div[4]/form/input[2]').click()

# 6. 等待商品名称出现并点击进入详情页
product_link = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[7]/div[2]/div[1]/div/form/div/div/div/p/a')))
product_link.click()

# 7. 等待“加入购物车”按钮出现并点击
add_to_cart = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[7]/div[2]/div[1]/div[2]/form/ul/li[9]/a[1]/img')))
add_to_cart.click()

# 8. 等待“删除”链接可点击后点击
delete_link = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[7]/div[1]/form/table[1]/tbody/tr[2]/td[7]/a')))
delete_link.click()

# 9. 等待删除确认 alert 弹出，打印内容并点击“取消”
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()

# 10. 关闭浏览器
driver.quit()
