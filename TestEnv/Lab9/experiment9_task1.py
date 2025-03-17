from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 设置Firefox驱动器
driver = webdriver.Firefox()

try:
    # 1. 打开ECSHOP前台首页
    driver.get("http://localhost/upload/index.php")

    # 2. 点击注册按钮并等待5秒
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/font/a[2]/img").click()
    time.sleep(5)

    # 3. 点击“用户协议”并等待8秒
    driver.find_element(By.XPATH, "/html/body/div[7]/div/form/table/tbody/tr[13]/td[2]/label/a").click()
    time.sleep(8)

    # 4. 获得当前窗口句柄
    main_window_handle = driver.current_window_handle

    # 5. 切换到最新窗口
    handles = driver.window_handles
    for handle in handles:
        if handle != main_window_handle:
            driver.switch_to.window(handle)

    # 6. 在新窗口里点击配送与支付按钮并等待5秒
    driver.find_element(By.XPATH, "/html/body/div[9]/div/div/dl[3]/dt/a").click()
    time.sleep(5)

    # 7. 点击“EC论坛”并等待5秒后切换到新窗口
    driver.find_element(By.XPATH, "/html/body/div[3]/a[11]").click()
    time.sleep(5)

    # 保存“EC论坛”的窗口句柄
    ec_forum_window_handle = driver.window_handles[-1]
    driver.switch_to.window(ec_forum_window_handle)

    # 8. 点击“商业授权”并等待5秒后切换到新窗口
    driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/a[2]").click()
    time.sleep(5)

    # 9. 关闭“EC论坛”窗口
    driver.close()

    # 10. 切换回原窗口
    driver.switch_to.window(main_window_handle)

    # 11. 输入用户名“Jack”并等待3秒
    driver.find_element(By.XPATH, "//*[@id='username']").send_keys("Jack")
    time.sleep(3)

finally:
    # 12. 关闭浏览器
    driver.quit()
