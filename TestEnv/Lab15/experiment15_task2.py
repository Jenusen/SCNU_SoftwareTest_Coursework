from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os
import time

# 设置Firefox下载文件的配置
options = Options()
download_dir = "c:\\temp"

# 配置下载目录
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", download_dir)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")

# 启动浏览器
driver = webdriver.Firefox(options=options)

# 打开下载页面
driver.get("http://sahitest.com/demo/saveAs.htm")

# 下载文件
download_link = driver.find_element(By.XPATH, "/html/body/a[1]")
download_link.click()

# 等待文件下载完成
time.sleep(5)

# 关闭浏览器
driver.quit()
