# -*- coding: utf-8 -*-
"""
功能：ECShop网站的自动化测试
时间：2024年5月26日
作者：20212005166洪梓腾
版本号：1.0
测试环境：Windows 10, Python 3.8, Selenium 4.1.0, Firefox浏览器
"""

from selenium import webdriver  # 导入Selenium的webdriver模块
from selenium.webdriver.common.by import By  # 导入By类，用于定位元素
from selenium.webdriver.common.keys import Keys  # 导入Keys类，用于模拟键盘按键
from selenium.webdriver.common.action_chains import ActionChains  # 导入ActionChains类，用于执行复杂的动作链
import time  # 导入time模块，用于控制等待时间
import ddddocr  # 导入ddddocr模块，用于验证码识别

# 初始化webdriver
driver = webdriver.Firefox()  # 启动Firefox浏览器

# 1. 打开首页，点击“登录”按钮，等待1秒
driver.get("http://localhost/upload/index.php")  # 打开首页
time.sleep(1)  # 等待页面加载
login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img')  # 定位登录按钮
login_button.click()  # 点击登录按钮
time.sleep(1)  # 等待页面跳转

# 2. 进行浏览器后退操作，截图
driver.back()  # 浏览器后退
time.sleep(1)  # 等待页面加载
driver.save_screenshot('页面操作截图/step1-后退操作-登录页到首页.png')  # 截图保存

# 3. 进行浏览器前进操作，截图
driver.forward()  # 浏览器前进
time.sleep(1)  # 等待页面加载
driver.save_screenshot('页面操作截图/step2-前进操作-首页到登录页.png')  # 截图保存

# 浏览器导航和窗口大小操作
# 4. 输出窗口位置，最小化窗口大小，自定义窗口位置，最大化窗口大小并截图
print(driver.get_window_position())  # 输出当前窗口的位置
driver.minimize_window()  # 最小化窗口
time.sleep(1)  # 等待窗口变化
driver.save_screenshot('页面操作截图/step3-最小化窗口.png')  # 截图保存

driver.set_window_position(100, 100)  # 设置窗口位置为(100, 100)
driver.set_window_size(800, 600)  # 设置窗口大小为800x600
time.sleep(1)  # 等待窗口变化
driver.save_screenshot('页面操作截图/step4-自定义窗口位置.png')  # 截图保存

driver.maximize_window()  # 最大化窗口
time.sleep(1)  # 等待窗口变化
driver.save_screenshot('页面操作截图/step5-最大化窗口大小.png')  # 截图保存

# 5. 获取用户名和密码标签，输入用户名和密码并登录，截图
username_label = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[1]/td[1]')  # 定位用户名标签
print(username_label.text)  # 输出用户名标签的文本
username_input = driver.find_element(By.XPATH,
                                     '/html/body/div[7]/div[1]/form/table/tbody/tr[1]/td[2]/input')  # 定位用户名输入框
username_input.send_keys('vip')  # 输入用户名
password_label = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[2]/td[1]')  # 定位密码标签
print(password_label.text)  # 输出密码标签的文本
password_input = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[2]/td[2]/input')  # 定位密码输入框
password_input.send_keys('vip')  # 输入密码
driver.save_screenshot('页面操作截图/step6-获取与处理数据并登录.png')  # 截图保存

login_button = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[3]/td[2]/input[3]')  # 定位登录按钮
login_button.click()  # 点击登录按钮
time.sleep(3)  # 等待登录完成

# 6. 切换到后台页面，截图
current_window = driver.current_window_handle  # 获取当前窗口句柄
driver.execute_script("window.open('http://localhost/upload/admin/privilege.php')")  # 打开后台页面的新窗口
new_window = driver.window_handles[-1]  # 获取新窗口句柄
driver.switch_to.window(new_window)  # 切换到新窗口
time.sleep(3)  # 等待页面加载
driver.save_screenshot('页面操作截图/step7-切换到后台页新窗口.png')  # 截图保存

# 7. 输入后台登录信息并截图
admin_username = driver.find_element(By.XPATH,
                                     '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input')  # 定位后台用户名输入框
admin_password = driver.find_element(By.XPATH,
                                     '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input')  # 定位后台密码输入框
admin_captcha = driver.find_element(By.XPATH,
                                    '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input')  # 定位后台验证码输入框

admin_username.send_keys('admin')  # 输入后台用户名
admin_password.send_keys('admin123')  # 输入后台密码
admin_captcha.send_keys('0')  # 输入万能验证码
driver.save_screenshot('页面操作截图/step8-输入后台页登录信息.png')  # 截图保存

# 8. 查看并操作“保存登录状态”按钮，双击、右击、确认操作并截图
remember_button = driver.find_element(By.XPATH, '//*[@id="remember"]')  # 定位“保存登录状态”按钮
print(remember_button.is_selected())  # 输出按钮的选中状态
ActionChains(driver).double_click(remember_button).perform()  # 双击按钮
time.sleep(1)  # 等待操作完成
driver.save_screenshot('页面操作截图/step9-页面双击操作.png')  # 截图保存
ActionChains(driver).context_click(remember_button).perform()  # 右击按钮
time.sleep(1)  # 等待操作完成
remember_button.click()  # 单击操作
time.sleep(1)
driver.save_screenshot('页面操作截图/step10-单选框单击确认操作.png')  # 截图保存

# 9. 进入管理中心，点击商品列表，切换frame并截图
confirm_button = driver.find_element(By.XPATH,
                                     '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[6]/td[2]/input')  # 定位确认按钮
confirm_button.click()  # 点击确认按钮
time.sleep(3)  # 等待操作完成
driver.save_screenshot('页面操作截图/step11-成功登录到后台.png')  # 截图保存

# 切换到menu-frame并点击商品列表
driver.switch_to.default_content()  # 切换回主frame
driver.switch_to.frame("menu-frame")  # 切换到menu-frame
driver.find_element(By.CSS_SELECTOR,
                    "li.explode:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > "
                    "a:nth-child(1)").click()  # 点击商品列表
time.sleep(5)  # 等待页面加载
driver.save_screenshot('页面操作截图/step12-切换frame.png')  # 截图保存

# 切换到main-frame并点击查看商品详情
driver.switch_to.default_content()  # 切换回主frame
driver.switch_to.frame("main-frame")  # 切换到main-frame
driver.find_element(By.XPATH, '/html/body/form/div[1]/table[1]/tbody/tr[3]/td[11]/a[1]/img').click()  # 点击查看商品详情
time.sleep(5)  # 等待页面加载

# 处理弹出的新窗口
back_manage_window = driver.current_window_handle
new_window = driver.window_handles[-1]  # 获取新窗口句柄
driver.switch_to.window(new_window)  # 切换到新窗口
checkbox = driver.find_element(By.XPATH, '//*[@id="spec_value_158"]')  # 定位蓝牙耳机复选框
if not checkbox.is_selected():  # 如果复选框未选中
    checkbox.click()  # 选中复选框

driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[1]/div[2]/form/ul/li[9]/a[2]/img').click()  # 点击加入收藏夹按钮
time.sleep(5)  # 等待操作完成
driver.switch_to.alert.accept()  # 接受弹窗
driver.close()  # 关闭当前窗口

# 切换回后台窗口，操作商品回收站和开店向导
driver.switch_to.window(back_manage_window)  # 切换回后台窗口
driver.switch_to.default_content()
driver.switch_to.frame("menu-frame")  # 切换到menu-frame
driver.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[1]/ul/li[7]/a').click()  # 点击商品回收站
time.sleep(5)  # 等待页面加载
driver.switch_to.default_content()  # 切换回主frame
driver.switch_to.frame("header-frame")  # 切换到header-frame
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/ul/li[9]/a').click()  # 点击开店向导按钮
time.sleep(5)  # 等待页面加载
driver.save_screenshot('页面操作截图/step13-切换到header-frame.png')  # 截图保存

driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/a[2]').click()  # 点击退出按钮
time.sleep(5)  # 等待操作完成

# 10. 跳转新页面并发表评论，识别验证码并截图
# 跳转到指定URL
driver.get('http://localhost/upload/goods.php?id=24')

email_input = driver.find_element(By.XPATH, '//*[@id="email"]')  # 定位邮箱输入框
comment_input = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div['
                                              '3]/form/table/tbody/tr[4]/td[2]/textarea')  # 定位评论输入框
captcha_img = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div['
                                            '3]/form/table/tbody/tr[5]/td/div/img')  # 定位验证码图片
captcha_input = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div['
                                              '3]/form/table/tbody/tr[5]/td/div/input')  # 定位验证码输入框

email_input.clear()
email_input.send_keys('a@b.com')  # 输入邮箱
comment_input.send_keys("It’s excellent")  # 输入评论内容

captcha_img.screenshot('check.png')  # 截取验证码图片
ocr = ddddocr.DdddOcr()  # 创建OCR对象
img_bytes = open('check.png', 'rb').read()  # 读取验证码图片
check_code = ocr.classification(img_bytes)  # 识别验证码
captcha_input.send_keys(check_code)  # 输入识别到的验证码
driver.save_screenshot('页面操作截图/step14-验证码获取与识别.png')  # 截图保存
driver.find_element(By.XPATH,
                    '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/input').click()  # 点击提交评论按钮
time.sleep(5)  # 等待操作完成
driver.switch_to.alert.accept()  # 接受弹窗
driver.close()  # 关闭当前窗口

# 11. 切换回最初窗口，进行留言操作并截图
driver.switch_to.window(current_window)  # 切换回最初窗口
# 点击上方“用户中心”
user_center = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/ul/li[1]/font/font/a[1]")
user_center.click()

# 等待3秒
time.sleep(3)

# 点击左侧“我的留言”
my_message = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div/div/div/div/a[6]")
my_message.click()

# 等待3秒
time.sleep(3)
# 输入主题
subject = driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/div/div/form/table/tbody/tr[2]/td[2]/input")
subject.send_keys("hello")
# 输入留言内容
message_content = driver.find_element(By.XPATH,
                                      "/html/body/div[7]/div[2]/div/div/div/form/table/tbody/tr[3]/td[2]/textarea")
message_content.send_keys("welcome to this world!")
# 选择文件
file_upload = driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/div/div/form/table/tbody/tr[4]/td[2]/input")
file_upload.send_keys("c:\\temp\\777.txt")
driver.save_screenshot('页面操作截图/step15-文件上传.png')  # 截图保存
# 点击“提交”
submit_button = driver.find_element(By.XPATH,
                                    "/html/body/div[7]/div[2]/div/div/div/form/table/tbody/tr[5]/td[2]/input[2]")
submit_button.click()

# 12. 退出浏览器
driver.quit()  # 关闭浏览器
