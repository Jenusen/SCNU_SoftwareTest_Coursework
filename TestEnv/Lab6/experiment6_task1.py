from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# 启动Firefox浏览器
driver = webdriver.Firefox()

try:
    # 打开前台首页
    driver.get("http://localhost/upload/index.php")

    # 输入关键字100
    search_input = driver.find_element(By.XPATH, "//*[@id='keyword']")
    search_input.send_keys("100")

    # 判断“搜索”按钮如果可用，点击搜索按钮
    search_button = driver.find_element(By.XPATH, "/html/body/div[4]/form/input[2]")
    if search_button.is_enabled():
        search_button.click()
        sleep(3)  # 等待3秒

    # 点击搜索结果区域里的“金立 A30”商品名称
    driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[1]/div/form/div/div/div[3]/p/a").click()
    sleep(3)  # 等待3秒

    # 打印默认“购买数量”文本框的当前默认值
    number_input = driver.find_element(By.XPATH, "//*[@id='number']")
    print(f"默认购买数量：{number_input.get_attribute('value')}")

    # 获得“商品库存”的台数
    stock = driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[1]/div[2]/form/ul/li[1]/dd[2]").text.split(" ")[1]
    stock = int(stock)
    print(f"商品库存：{stock} 台")

    # 如果台数大于3台，清空“购买数量”文本框，输入3
    if stock > 3:
        number_input.clear()
        number_input.send_keys("3")

    # 判断“数据线”复选框，如果没有被选中，就点击选中它
    data_line_checkbox = driver.find_element(By.XPATH, "//*[@id='spec_value_190']")
    if not data_line_checkbox.is_selected():
        data_line_checkbox.click()

    # 判断“线控耳机”复选框，如果没有被选中，就点击选中它
    earphones_checkbox = driver.find_element(By.XPATH, "//*[@id='spec_value_189']")
    if not earphones_checkbox.is_selected():
        earphones_checkbox.click()

    # 获得此时的“商品总价”
    total_price = driver.find_element(By.XPATH, "//*[@id='ECS_GOODS_AMOUNT']").text
    print(f"商品总价：{total_price}")

    # 判断总价是否计算正确
    if total_price == "￥6210元":
        print("总价计算正确")
    else:
        print("总价计算错误")
finally:
    # 测试完成后关闭浏览器
    driver.quit()
