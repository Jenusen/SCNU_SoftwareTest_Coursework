from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    # 初始化Firefox浏览器
    driver = webdriver.Firefox()
    driver.get("http://localhost/upload/admin/index.php")

    # 输入用户名
    username = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input")
    username.send_keys("admin")

    # 输入密码
    password = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input")
    password.send_keys("admin123")

    # 输入验证码
    captcha = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input")
    captcha.send_keys("0")

    # 点击进入管理中心
    login_button = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[6]/td[2]/input")
    login_button.click()
    time.sleep(8)

    # 切换到左侧菜单frame
    driver.switch_to.frame("menu-frame")

    # 点击商品列表
    product_list_link = driver.find_element(By.CSS_SELECTOR,
                                            "li.explode:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)")
    product_list_link.click()
    time.sleep(5)

    # 切换回主frame
    driver.switch_to.default_content()
    # 切换到商品列表的frame
    driver.switch_to.frame("main-frame")
    # 点击查看诺基亚N85
    view_nokia = driver.find_element(By.XPATH, "/html/body/form/div[1]/table[1]/tbody/tr[3]/td[11]/a[1]/img")
    view_nokia.click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    # 检查蓝牙耳机复选框是否选中
    bluetooth_checkbox = driver.find_element(By.XPATH, "//*[@id='spec_value_158']")
    if not bluetooth_checkbox.is_selected():
        bluetooth_checkbox.click()

    # 点击加入收藏夹
    add_to_favorites = driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[1]/div[2]/form/ul/li[9]/a[2]/img")
    add_to_favorites.click()
    # 处理弹窗
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(5)

    # 关闭诺基亚N85窗口并返回
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    # 切换到左侧菜单frame
    driver.switch_to.default_content()
    driver.switch_to.frame("menu-frame")

    # 点击商品回收站
    recycle_bin_link = driver.find_element(By.CSS_SELECTOR,
                                           "li.explode:nth-child(1) > ul:nth-child(1) > li:nth-child(7) > a:nth-child(1)")
    recycle_bin_link.click()
    time.sleep(5)

    # 切换回主frame
    driver.switch_to.default_content()
    driver.switch_to.frame("main-frame")

    # 切换到头部frame
    driver.switch_to.default_content()
    driver.switch_to.frame("header-frame")

    # 点击开店向导
    store_guide_link = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/ul/li[9]/a")
    store_guide_link.click()
    time.sleep(5)

    # 点击退出
    logout_link = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/a[2]")
    logout_link.click()
    time.sleep(5)

    # 输入管理员姓名
    driver.switch_to.default_content()
    admin_name = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input")
    admin_name.send_keys("Jack")

finally:
    # 关闭浏览器
    driver.quit()
