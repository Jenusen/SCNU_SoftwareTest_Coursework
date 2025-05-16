from io import BytesIO

import ddddocr
import requests
from PIL import Image
from PIL.ImageFilter import RankFilter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import pytesseract
import time

# from TestEnv.operation.operation import captcha_img, captcha_input

# === 初始化浏览器，进入 ECShop 首页 ===
driver = webdriver.Firefox()
driver.get("http://localhost/upload/index.php")

# === 示例代码：浏览器窗口操作和前进后退操作（可选） ===
# driver.set_window_size(1200, 800)
# driver.set_window_position(120, 120)
# driver.maximize_window()
# time.sleep(1)

# GSM_XPATH = "/html/body/div[3]/a[2]"
# driver.find_element(By.XPATH, GSM_XPATH).click()
# time.sleep(3)
# driver.back()
# time.sleep(1)
# driver.forward()
# time.sleep(1)

# === 示例：搜索商品名称 ===
# FIRST_PHONE_XPATH = "/html/body/div[7]/div[2]/div[5]/div/form/div/div/div[1]/p/a"
# phone_name = driver.find_element(By.XPATH, FIRST_PHONE_XPATH).text
# search_input = driver.find_element(By.NAME, "keywords")
# search_input.send_keys(phone_name)
# search_button = driver.find_element(By.NAME, "imageField")
# search_button.click()
# time.sleep(3)

# === 1. 打开后台页面 ===
driver.execute_script("window.open('http://localhost/upload/admin/privilege.php')")
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
driver.switch_to.window(driver.window_handles[-1])
WebDriverWait(driver, 10).until(EC.title_contains("ECSHOP"))

# === 2. 输入后台登录信息并截图 ===
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input'))
)
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input').send_keys('admin')
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input').send_keys('admin123')
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input').send_keys('0')
driver.save_screenshot('Screenshot/step8-输入后台页登录信息.png')

# === 3. 操作“保存登录状态”复选框并右键 ===
remember_btn = driver.find_element(By.ID, 'remember')
print("初始状态:", remember_btn.is_selected())
remember_btn.click()
time.sleep(1)
print("点击后状态:", remember_btn.is_selected())
driver.save_screenshot('Screenshot/step9-页面双击操作.png')
ActionChains(driver).context_click(remember_btn).perform()
time.sleep(1)
remember_btn.click()
time.sleep(1)
driver.save_screenshot('Screenshot/step10-单选框单击确认操作.png')

# === 4. 登录后台并进入商品品牌 ===
confirm_button = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[6]/td[2]/input')
confirm_button.click()
WebDriverWait(driver, 10).until(EC.title_contains("管理中心"))
driver.save_screenshot('Screenshot/step11-成功登录到后台.png')

# === 5. 切换 frame，点击商品品牌 ===
driver.switch_to.default_content()
driver.switch_to.frame("menu-frame")
driver.find_element(By.CSS_SELECTOR, "li.explode:nth-child(1) > ul:nth-child(1) > li:nth-child(5) > a:nth-child(1)").click()
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) >= 1)
driver.save_screenshot('Screenshot/step12-切换frame.png')

# === 6. 点击查看品牌详情，进入新窗口 ===
driver.switch_to.default_content()
driver.switch_to.frame("main-frame")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/form/div/table/tbody/tr[2]/td[2]/a'))
)
driver.find_element(By.XPATH, '/html/body/form/div/table/tbody/tr[2]/td[2]/a').click()
back_manage_window = driver.current_window_handle
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
new_window = [w for w in driver.window_handles if w != back_manage_window][0]
driver.switch_to.window(new_window)
driver.close()  # 关闭新打开的详情窗口
driver.switch_to.window(back_manage_window)

# === 7. 回到后台页面，打开记事本页面 ===
driver.switch_to.default_content()
driver.switch_to.frame("menu-frame")
# 截图调试
driver.save_screenshot('debug-notepad.png')
print("当前所有frame句柄：", driver.window_handles)
print("已切入menu-frame")
driver.switch_to.default_content()
frames = driver.find_elements(By.TAG_NAME, 'frame')

for i in range(len(frames)):
    driver.switch_to.default_content()
    driver.switch_to.frame(frames[i])
    print(f"正在检查第 {i} 个 frame")
    try:
        button = driver.find_element(By.XPATH, '//a[contains(text(), "记事本")]')
        print(f"✅ 在第 {i} 个 frame 找到了按钮: {button.text}")
        button.click()
        break
    except:
        print(f"❌ 第 {i} 个 frame 没找到")

# === 8. 切换 frame，复制品牌描述文本 ===
driver.switch_to.default_content()
driver.switch_to.frame("main-frame")

Nokia_Comment_XPath = "/html/body/form/div/table/tbody/tr[2]/td[3]"
nokia_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, Nokia_Comment_XPath))
)

# 双击选中并复制文本
ActionChains(driver).move_to_element(nokia_element).double_click().perform()
time.sleep(1)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
time.sleep(1)

# === 9. 找到输入框并粘贴文本 ===
input_xpath = '/html/body/div[4]/div/div[2]/textarea'  # 请根据页面结构修改
elements = driver.find_elements(By.XPATH, input_xpath)
print(f"找到 {len(elements)} 个匹配 input")
for e in elements:
    print(e.get_attribute('outerHTML'))

target_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, input_xpath)))
target_input.send_keys("测试内容")


driver.switch_to.default_content()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it("main-frame"))

target_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, input_xpath)))
target_input.click()
time.sleep(0.5)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

# === 10. 点击保存按钮 ===
text_save_Xpath = "/html/body/div[4]/div/div[3]/div[1]/input[1]"
text_save = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, text_save_Xpath)))
text_save.click()

time.sleep(5)


# # === 当前主流程：新开页面并跳转至“手机常识”栏目，提交评论，处理弹窗 ===
#
# # 打开新标签页并切换
# driver.execute_script("window.open('http://localhost/upload/index.php')")
# WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
# driver.switch_to.window(driver.window_handles[-1])
#
# # 点击“手机常识”链接
# COMMON_KNOWLEDGE_XPATH = "/html/body/div[8]/div/div/dl[2]/dd[1]/a"
# common_kl = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, COMMON_KNOWLEDGE_XPATH))
# )
# common_kl.click()
# time.sleep(1)
##########
# # 点击“提交评论”按钮
# SUBMIT_REVIEW_XPATH = "/html/body/div[7]/div[2]/div[3]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/input"
# submit_btn = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, SUBMIT_REVIEW_XPATH))
# )
# submit_btn.click()
#
# # 检测并处理弹窗（截图+确认）
# try:
#     WebDriverWait(driver, 10).until(EC.alert_is_present())
#     # driver.save_screenshot("Screenshot/alert出现时的截图.png")
#     alert = driver.switch_to.alert
#     print("弹窗内容：", alert.text)
#     time.sleep(3)
#     alert.accept()
# except NoAlertPresentException:
#     print("没有弹窗出现")
##########

# # 填写邮箱
# email_input = driver.find_element(By.NAME, "email")
# email_input.send_keys("88888888@qq.com")
#
# # 选择五分好评
# rank5_radio = driver.find_element(By.ID, "comment_rank5")
# rank5_radio.click()
#
# # 输入评论内容
# content_input = driver.find_element(By.NAME, "content")
# content_input.send_keys("20222034046，666")
#
# # 获取验证码图片元素
# captcha_img = driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[3]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/div/img")
#
# # ✅ 用 Selenium 直接截图验证码（确保和页面一致）
# captcha_img.screenshot("Screenshot/check.png")

# # 使用 ddddocr 识别验证码
# import ddddocr
# ocr = ddddocr.DdddOcr()
# with open("Screenshot/check.png", "rb") as f:
#     img_bytes = f.read()
# check_code = ocr.classification(img_bytes)
#
# print("识别到的验证码是：", check_code)
#
# # 输入验证码
# captcha_input = driver.find_element(By.NAME, "captcha")
# captcha_input.send_keys(check_code)
#
# # 截图保存调试信息
# driver.save_screenshot('Screenshot/step14-验证码获取与识别.png')
#
# # 提交按钮
# submit_button = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[2]/div[3]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/input"))
# )
# submit_button.click()
#
# # 检测并处理弹窗（截图+确认）
# try:
#     WebDriverWait(driver, 10).until(EC.alert_is_present())
#     alert = driver.switch_to.alert
#     print("弹窗内容：", alert.text)
#     time.sleep(3)
#     alert.accept()
# except NoAlertPresentException:
#     print("没有弹窗出现")
##########
