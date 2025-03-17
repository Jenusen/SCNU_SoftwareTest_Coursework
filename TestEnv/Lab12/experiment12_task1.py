from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# 启动Firefox浏览器
driver = webdriver.Firefox()

# 打开ECShop后台页
driver.get("http://localhost/upload/admin/index.php")

# 输入用户名
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input').send_keys('admin')
# 输入密码
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input').send_keys('admin123')
# 输入万能验证码
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input').send_keys('0')

# 勾选记住我
remember_checkbox = driver.find_element(By.XPATH, '//*[@id="remember"]')
if not remember_checkbox.is_selected():
    remember_checkbox.click()

# 点击“进入管理中心”
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[6]/td[2]/input').click()

# 等待8秒
time.sleep(8)

# 切换到header-frame
driver.switch_to.default_content()
driver.switch_to.frame("header-frame")

# 点击“个人设置”
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/ul/li[6]/a').click()

# 等待5秒
time.sleep(5)

# 切换到main-frame
driver.switch_to.default_content()
driver.switch_to.frame("main-frame")

# 选中“设置个人导航”右侧下拉列表的从第1个到第6个选项
right_select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/form/table/tbody/tr[6]/td[2]/table/tbody/tr/td[3]/select'))
for i in range(6):
    right_select.select_by_index(i)
time.sleep(5)

# 取消第2个选项
right_select.deselect_by_index(1)
time.sleep(5)

# 取消右侧下拉列表所有选项
right_select.deselect_all()

# 选择右侧文本是“商品类型”的选项
for option in right_select.options:
    if option.text.strip() == "商品类型":
        option.click()
        break
time.sleep(3)

# 如果“增加”按钮变为可用，点击它
add_button = driver.find_element(By.XPATH, '//*[@id="btnAdd"]')
if add_button.is_enabled():
    add_button.click()
    time.sleep(5)

# 选中“设置个人导航”左侧下拉列表的最后一个选项和倒数第二个选项
left_select = Select(driver.find_element(By.XPATH, '/html/body/div[1]/form/table/tbody/tr[6]/td[2]/table/tbody/tr/td[1]/select'))
left_select.select_by_index(len(left_select.options) - 1)
left_select.select_by_index(len(left_select.options) - 2)
time.sleep(3)

# 打印左侧下拉列表中所有已被选中的选项的文本
selected_options = [option.text for option in left_select.all_selected_options]
print("所有已被选中的选项:", selected_options)

# 打印左侧下拉列表中已被选中的选项中第一个的文本
if selected_options:
    print("第一个已被选中的选项:", selected_options[0])

# 关闭浏览器
driver.quit()
