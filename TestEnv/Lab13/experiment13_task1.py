from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# 创建截图保存目录
if not os.path.exists('screenshot'):
    os.makedirs('screenshot')

# 初始化浏览器
driver = webdriver.Firefox()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import os

# 创建截图保存目录
if not os.path.exists('screenshot'):
    os.makedirs('screenshot')

# 初始化浏览器
driver = webdriver.Firefox()

try:
    # 1. 打开后台登陆页
    driver.get('http://localhost/upload/admin/index.php')
    time.sleep(3)

    # 2. 输入用户名、密码和万能验证码，等待3秒，进行截屏
    driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input').send_keys('admin')
    driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input').send_keys('admin123')
    driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input').send_keys('0')
    time.sleep(3)
    driver.save_screenshot('screenshot/step2.png')

    # 3. 勾选单选框并点击“进入管理中心”，等待5秒，进行截屏
    remember_checkbox = driver.find_element(By.XPATH, '//*[@id="remember"]')
    if not remember_checkbox.is_selected():
        remember_checkbox.click()
    driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[6]/td[2]/input').click()
    time.sleep(5)
    driver.save_screenshot('screenshot/step3.png')

    # 4. 对左侧菜单栏进行截屏（切换到menu-frame的frame中）
    driver.switch_to.default_content()
    driver.switch_to.frame('menu-frame')
    driver.save_screenshot('screenshot/step4.png')

    # 5. 点击“商品列表”，等待3秒，对右侧商品列表区域进行截屏（切换到main-frame的frame中）
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[1]/ul/li[1]/a').click()
    time.sleep(3)
    driver.switch_to.default_content()
    driver.switch_to.frame('main-frame')
    driver.save_screenshot('screenshot/step5.png')

    # 6. 点击商品列表中“夏新N7”一行中的查看按钮，等待3秒，切换到新窗口，对新窗口进行截屏
    driver.find_element(By.XPATH, '/html/body/form/div[1]/table[1]/tbody/tr[11]/td[11]/a[1]/img').click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    driver.save_screenshot('screenshot/step6.png')

    # 7. 点击登录按钮，等待3秒，进行截屏
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
    time.sleep(3)
    driver.save_screenshot('screenshot/step7.png')

    # 8. 点击“立即登陆”按钮，等待2秒，进行截屏
    driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[3]/td[2]/input[3]').click()
    time.sleep(2)

    # 9. 对弹出来的消息框点击确认
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        print("No alert to accept")

    # 10. 输入用户名：vip，输入密码：vip
    driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[1]/td[2]/input').send_keys('vip')
    driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[2]/td[2]/input').send_keys('vip')

    # 11. 点击“立即登陆”按钮，等待3秒，进行截屏
    driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[3]/td[2]/input[3]').click()
    time.sleep(3)
    driver.save_screenshot('screenshot/step11.png')

    # 12. 自动刷新页面后，对包含ECSHOP图标在内的最上侧区域进行截屏
    time.sleep(3)
    driver.save_screenshot('screenshot/step12.png')

finally:
    # 13. 关闭浏览器
    driver.quit()
