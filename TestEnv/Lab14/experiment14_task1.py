from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
import time

# 初始化 Firefox 浏览器
driver = webdriver.Firefox()

try:
    # 打开商品详情页
    driver.get('http://localhost/upload/goods.php?id=24')

    # 输入 E-mail
    email_element = driver.find_element(By.XPATH, '//*[@id="email"]')
    email_element.send_keys('a@b.com')

    # 输入评论内容
    comment_element = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div[3]/form/table/tbody/tr[4]/td[2]/textarea')
    comment_element.send_keys("It’s excellent")

    # 定位并截图验证码图片
    captcha_image_element = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/div/img')
    captcha_image_path = 'check.png'
    captcha_image_element.screenshot(captcha_image_path)

    # 读取图片文件的字节
    with open(captcha_image_path, 'rb') as f:
        img_bytes = f.read()

    # 创建 OCR 对象并识别验证码
    ocr = ddddocr.DdddOcr()
    check_code = ocr.classification(img_bytes)
    print(f"识别的验证码是: {check_code}")

    # 输入正确的验证码
    captcha_input_element = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/div/input')
    captcha_input_element.send_keys(check_code)

    # 点击提交评论按钮
    submit_button_element = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/input')
    submit_button_element.click()

    # 等待几秒钟以观察结果
    time.sleep(5)

finally:
    # 关闭浏览器
    driver.quit()
