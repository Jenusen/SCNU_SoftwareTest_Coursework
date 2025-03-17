from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# 启动Firefox浏览器
driver = webdriver.Firefox()

try:
    # 登录前台首页
    driver.get("http://localhost/upload/index.php")

    # 点击“留言板”
    driver.find_element(By.XPATH, "/html/body/div[3]/a[10]").click()

    # 定位电子邮件地址文本框并输入电子邮件地址
    email_input = driver.find_element(By.XPATH,
                                      "/html/body/div[7]/div[2]/div[4]/div/div/form/table/tbody/tr[2]/td[2]/input")
    email_input.send_keys("vip@ecshop.com")

    # 按下Home键光标回到行首
    email_input.send_keys(Keys.HOME)

    # Shift+右箭头（→）连续点击三次，选中三个字符vip
    for _ in range(3):
        email_input.send_keys(Keys.SHIFT + Keys.RIGHT)

    # Ctrl+c复制
    email_input.send_keys(Keys.CONTROL, 'c')

    # 到主题文本框里Ctrl+v粘贴
    subject_input = driver.find_element(By.XPATH,
                                        "/html/body/div[7]/div[2]/div[4]/div/div/form/table/tbody/tr[4]/td[2]/input")
    subject_input.send_keys(Keys.CONTROL, 'v')

    # 到留言内容里输入“我是”、Ctrl+v粘贴，Enter回车换行
    message_input = driver.find_element(By.XPATH,
                                        "/html/body/div[7]/div[2]/div[4]/div/div/form/table/tbody/tr[5]/td[2]/textarea")
    message_input.send_keys("我是")
    message_input.send_keys(Keys.CONTROL, 'v')
    message_input.send_keys(Keys.ENTER)

    # 再输入“请问有优惠码？”
    message_input.send_keys("请问有优惠码？")
    sleep(5)
    # 在主题文本框里按下回车
    subject_input.send_keys(Keys.ENTER)

finally:
    # 暂停几秒让你看到效果后关闭浏览器
    sleep(5)
    driver.quit()
