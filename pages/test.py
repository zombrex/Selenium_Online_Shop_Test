import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
service=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = 'https://mixpcshop.ru/catalog/videokartyive/'
driver.get(url)
time.sleep(10)
item_title = driver.find_element(By.XPATH, "//div[@class='item-title']//span").text
cart = "//div[@class='wrap_icon inner-table-block top_basket']//i"
#driver.find_element(By.XPATH, cart).click()
#total_price = "//div[@class='basket-coupon-block-total-price-current']"
#get_total_price = driver.find_element(By.XPATH, total_price).text
#numbers = ''.join(c if c.isdigit() else '' for c in get_total_price)
print(item_title)
time.sleep(2)