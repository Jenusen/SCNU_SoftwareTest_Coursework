from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 设置Firefox驱动器
driver = webdriver.Firefox()

try:
    wait = WebDriverWait(driver, 10)  # 最多等待10秒

    # 1. 打开ECSHOP前台首页
    driver.get("http://localhost/upload/index.php")

    # 2. 点击注册按钮
    register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/font/a[2]/img")))
    register_button.click()
    time.sleep(5)

    # 3. 点击“用户协议”
    user_agreement_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/form/table/tbody/tr[13]/td[2]/label/a")))
    user_agreement_link.click()
    time.sleep(8)

    # 4. 获得当前窗口句柄
    main_window_handle = driver.current_window_handle

    # 5. 切换到最新窗口
    handles = driver.window_handles
    for handle in handles:
        if handle != main_window_handle:
            driver.switch_to.window(handle)

    # 6. 在新窗口里点击配送与支付按钮
    delivery_payment_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div/dl[3]/dt/a")))
    delivery_payment_button.click()
    time.sleep(5)

    # 7. 点击“EC论坛”
    ec_forum_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/a[11]")))
    ec_forum_link.click()
    time.sleep(5)

    # 保存“EC论坛”的窗口句柄
    ec_forum_window_handle = driver.window_handles[-1]
    driver.switch_to.window(ec_forum_window_handle)

    # 8. 点击“商业授权”
    business_auth_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[1]/div/a[2]")))
    business_auth_link.click()
    time.sleep(5)

    # 9. 关闭“EC论坛”窗口
    driver.close()

    # 10. 切换回原窗口
    driver.switch_to.window(main_window_handle)

    # 11. 输入用户名“Jack”
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='username']")))
    username_input.send_keys("Jack")
    time.sleep(3)

finally:
    # 12. 关闭浏览器
    driver.quit()
