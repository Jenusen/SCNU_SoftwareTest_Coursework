from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 启动Firefox浏览器
driver = webdriver.Firefox()

# 1.打开留言板页，等待3秒
driver.get("http://localhost/upload/message.php")
sleep(3)

# 2.设置浏览器窗口大小，等待3秒
driver.set_window_size(800, 600)
sleep(3)

# 3.打印窗口左上角位置坐标
print("Window position:", driver.get_window_position())

# 4.把浏览器窗口最小化，等待3秒，打印窗口大小尺寸
driver.minimize_window()
sleep(3)
print("Minimized window size:", driver.get_window_size())

# 5.自定义浏览器窗口位置，等待3秒
driver.set_window_position(60, 60)
sleep(3)
print("Custom window position:", driver.get_window_position())

# 6.把浏览器窗口最大化，等待3秒
driver.maximize_window()
sleep(3)
print("Maximized window size:", driver.get_window_size())

# 7.点击“高级搜索“，等待3秒
driver.find_element(By.XPATH, "/html/body/div[4]/form/a").click()
sleep(3)

# 8.后退，等待3秒
driver.back()
sleep(3)

# 9.获取当前网页的标题和URL，并打印
print("Page title:", driver.title)
print("Page URL:", driver.current_url)

# 10.前进，等待3秒
driver.forward()
sleep(3)

# 11.在地址栏输入获取的URL网址进行访问，等待3秒
driver.get(driver.current_url)
sleep(3)

# 12.后退，等待3秒
driver.back()
sleep(3)

# 13.关闭浏览器
driver.quit()
