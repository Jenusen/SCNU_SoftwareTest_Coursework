import pyperclip

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

# === 初始化浏览器，进入 ECShop 首页 ===
driver = webdriver.Firefox()
driver.get("http://localhost/upload/index.php")

# === 浏览器窗口操作 ===
driver.set_window_size(1200, 800)       # 设置浏览器窗口大小
driver.set_window_position(120, 120)    # 设置窗口位置
driver.maximize_window()                 # 最大化浏览器窗口
time.sleep(1)

# === 浏览器前进后退操作 ===
# 浏览器点击链接，测试前进后退功能
GSM_XPATH = "/html/body/div[3]/a[2]"
driver.save_screenshot('Screenshot/01-进入页面.png')  # 页面截图
driver.find_element(By.XPATH, GSM_XPATH).click()
time.sleep(3)
driver.back()     # 浏览器后退
driver.save_screenshot('Screenshot/02-浏览器后退页面.png')  # 页面截图
time.sleep(1)
driver.forward()  # 浏览器前进
driver.save_screenshot('Screenshot/03-浏览器前进页面.png')  # 页面截图
time.sleep(1)

# === 获取页面静态文本内容 & 输入框赋值操作示例 ===
Phone01_XPath = "/html/body/div[7]/div[2]/div[5]/div/form/div/div/div[1]/p/a"
phone_name = driver.find_element(By.XPATH, Phone01_XPath).text  # 获取商品名称文本
search_input = driver.find_element(By.NAME, "keywords")            # 定位搜索输入框
search_input.send_keys(phone_name)                                 # 输入获取的商品名称
driver.save_screenshot('Screenshot/04-输入获取页面静态文本的商品名称.png')  # 页面截图
search_button = driver.find_element(By.NAME, "imageField")         # 定位搜索按钮
search_button.click()
time.sleep(3)
driver.save_screenshot('Screenshot/05-得到搜索结果.png')  # 页面截图

# === 新开后台管理页面标签，并切换窗口 ===
driver.execute_script("window.open('http://localhost/upload/admin/privilege.php')")
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
driver.switch_to.window(driver.window_handles[-1])   # 切换到新打开窗口
WebDriverWait(driver, 10).until(EC.title_contains("ECSHOP"))
driver.save_screenshot('Screenshot/06-切换窗口.png')  # 页面截图

# === 登录后台：等待元素，输入账号密码及验证码，截图保存 ===
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input'))
)
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input').send_keys('admin')     # 输入用户名
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input').send_keys('admin123') # 输入密码
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input').send_keys('0')          # 输入验证码
driver.save_screenshot('Screenshot/07-输入后台登录信息.png')  # 页面截图

# === 获取复选框状态 ===
# === 操作“保存登录状态”复选框 ===
# === 模拟鼠标的单击，右键点击 ===
remember_btn = driver.find_element(By.ID, 'remember')
print("初始状态:", remember_btn.is_selected())  # 获取复选框是否被选中
remember_btn.click()                             # 点击复选框，切换状态
time.sleep(1)
print("点击后状态:", remember_btn.is_selected())
driver.save_screenshot('Screenshot/09-单选框单击确认操作.png')  # 截图保存当前状态
ActionChains(driver).context_click(remember_btn).perform()   # 模拟右键点击复选框
time.sleep(1)
remember_btn.click()  # 再次点击复选框切换状态
time.sleep(1)
driver.save_screenshot('Screenshot/10-单选框再次单击确认操作.png')  # 截图

# === 点击登录按钮，等待登录成功跳转页面，截图 ===
confirm_button = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[6]/td[2]/input')
confirm_button.click()
WebDriverWait(driver, 10).until(EC.title_contains("管理中心"))
driver.save_screenshot('Screenshot/11-成功登录后台.png')

# === 切换 frame 到菜单栏，点击商品品牌链接 ===
driver.switch_to.default_content()       # 切换到默认内容（主文档）
driver.switch_to.frame("menu-frame")     # 切换到名为menu-frame的frame
driver.find_element(By.CSS_SELECTOR, "li.explode:nth-child(1) > ul:nth-child(1) > li:nth-child(5) > a:nth-child(1)").click()
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) >= 1)
driver.save_screenshot('Screenshot/12-切换frame.png')

# === 切换到 main-frame，点击查看品牌详情，打开新窗口 ===
driver.switch_to.default_content()
driver.switch_to.frame("main-frame")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/form/div/table/tbody/tr[2]/td[2]/a'))
)
driver.find_element(By.XPATH, '/html/body/form/div/table/tbody/tr[2]/td[2]/a').click()

back_manage_window = driver.current_window_handle
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
new_window = [w for w in driver.window_handles if w != back_manage_window][0]

driver.switch_to.window(new_window)  # 切换到新窗口
driver.close()                       # 关闭新窗口
driver.switch_to.window(back_manage_window)  # 切回后台主窗口

# === 在多个 frame 中查找包含“记事本”按钮的frame并点击 ===
driver.switch_to.default_content()
frames = driver.find_elements(By.TAG_NAME, 'frame')

for i, frame in enumerate(frames):
    driver.switch_to.default_content()
    driver.switch_to.frame(frame)
    print(f"正在检查第 {i} 个 frame")
    try:
        button = driver.find_element(By.XPATH, '//a[contains(text(), "记事本")]')
        print(f"在第 {i} 个 frame 找到了按钮: {button.text}")
        button.click()
        break
    except Exception:
        print(f"第 {i} 个 frame 没找到")

driver.save_screenshot('Screenshot/13-打开文本框.png')

# === 切换到 main-frame，复制品牌描述文本（双击选中文本，模拟键盘的Ctrl+C复制,Ctrl+V粘贴及输入操作） ===
# === 模拟键盘的Ctrl+C复制,Ctrl+V粘贴及输入操作 ===
# === 模拟鼠标双击 ===
driver.switch_to.default_content()
driver.switch_to.frame("main-frame")

Nokia_Comment_XPath = "/html/body/form/div/table/tbody/tr[2]/td[3]"
nokia_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, Nokia_Comment_XPath))
)

# 模拟鼠标双击选中文本
ActionChains(driver).move_to_element(nokia_element).double_click().perform()
time.sleep(1)
# 模拟 Ctrl+C 复制选中文本
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

text_to_copy = nokia_element.text  # 直接获取文本内容
print(text_to_copy)

pyperclip.copy(text_to_copy)       # 复制文本到系统剪贴板
time.sleep(1)

# === 切换到含输入框的 frame，粘贴文本 ===
driver.switch_to.default_content()
frames = driver.find_elements(By.TAG_NAME, "frame")

# 选中第4个frame（从0开始计数）
driver.switch_to.frame(frames[3])
input_xpath = '//textarea'
target_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, input_xpath)))
target_input.clear()     # 清空输入框
target_input.click()
time.sleep(0.5)
# 模拟 Ctrl+V 粘贴文本
ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
driver.save_screenshot('Screenshot/14-模拟键盘将内容粘贴到文本框中.png')

# === 点击保存按钮 ===
text_save_xpath = "/html/body/div[4]/div/div[3]/div[1]/input[1]"
text_save = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, text_save_xpath)))
text_save.click()

time.sleep(5)

# === 打开新页面，跳转到“手机常识”栏目并提交评论，处理弹窗 ===
driver.execute_script("window.open('http://localhost/upload/index.php')")
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
driver.switch_to.window(driver.window_handles[-2])
driver.save_screenshot('Screenshot/15-切换到新页面.png')

# 点击“手机常识”链接
Common_Knowledge_XPath = "/html/body/div[8]/div/div/dl[2]/dd[1]/a"
common_kl = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, Common_Knowledge_XPath))
)
common_kl.click()
time.sleep(1)

# 点击“提交评论”按钮
Submit_Review_XPath = "/html/body/div[7]/div[2]/div[3]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/input"
submit_btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, Submit_Review_XPath))
)
submit_btn.click()

# 检测弹窗，截屏并确认
try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("弹窗内容：", alert.text)
    time.sleep(3)
    alert.accept()   # 点击弹窗“确定”
except NoAlertPresentException:
    print("没有弹窗出现")

# 填写邮箱
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("88888888@qq.com")

# 选择五分好评单选按钮
rank5_radio = driver.find_element(By.ID, "comment_rank5")
rank5_radio.click()

# 输入评论内容
content_input = driver.find_element(By.NAME, "content")
content_input.send_keys("20222034046，666")

# === 获取验证码操作 ===
captcha_img = driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[3]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/div/img")

# 用 Selenium 直接截图验证码（确保和页面一致）
captcha_img.screenshot("Screenshot/captcha.png")

# 使用 ddddocr 识别验证码
import ddddocr
ocr = ddddocr.DdddOcr()
with open("Screenshot/captcha.png", "rb") as f:
    img_bytes = f.read()
check_code = ocr.classification(img_bytes)

print("识别到的验证码是：", check_code)

# 输入验证码
captcha_input = driver.find_element(By.NAME, "captcha")
captcha_input.send_keys(check_code)

# 截图保存调试信息
driver.save_screenshot('Screenshot/16-验证码获取与识别.png')

# 提交按钮
submit_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[2]/div[3]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/input"))
)
submit_button.click()

# 检测并处理弹窗（截图+确认）
try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("弹窗内容：", alert.text)
    time.sleep(3)
    alert.accept()
except NoAlertPresentException:
    print("没有弹窗出现")