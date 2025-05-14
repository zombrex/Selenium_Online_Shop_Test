import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.order_page import Order_page
from pages.finish_page import Finish_page
from pages.category_page import Category_page

from pages.login_page import Login_page
from pages.main_page import Main_page


from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
service=Service(ChromeDriverManager().install())


# Тест 1 с выбором категории Процессоры
def test_buy_product_1():
   driver = webdriver.Chrome(service=service)

   """Авторизация пользователя"""

   #login = Login_page(driver)
   #login.authorization()

   """Главная страница - выбор категории (Процессоры, Видеокарты и тд)"""

   mp = Main_page(driver)
   mp.choose_category('Процессоры')

   """Страница выбранной категории - каталог товаров"""
   """Выбор товаров"""

   cat_p = Category_page(driver)

   cat_product_title = cat_p.select_products_1()

   """Страница корзины"""
   """Подтверждение выбора товаров"""

   cp = Cart_page(driver)
   cp.assert_item_title(cat_product_title)
   cp.assert_price()

   cp.product_confirm()

   """Страница оформления заказа"""
   """Ввод данных, подтверждение заказа."""

   # cip = Order_page(driver)
   # cip.input_information()

   """Страница с одобрением заказа"""

   # f = Finish_page(driver)
   # f.finish()

   time.sleep(3)
   driver.quit()


# Тест 2 с выбором категории Видеокарты
# def test_buy_product_2():
#    driver = webdriver.Chrome(service=service)
#    print("Start Test 1")
#
#    """Авторизация пользователя"""
#
#    #login = Login_page(driver)
#    #login.authorization()
#
#    """Главная страница - выбор категории (Процессоры, Видеокарты и тд)"""
#
#    mp = Main_page(driver)
#    mp.choose_category('Видеокарты')
#
#    """Страница выбранной категории - каталог товаров"""
#    """Выбор товаров"""
#
#    cat_p = Category_page(driver)
#    cat_p.select_products_2()
#
#    """Страница корзины"""
#    """Подтверждение выбора товаров"""
#    cp = Cart_page(driver)
#    cp.assert_price()
#
#    print(cat_product_title)
#    print(cp.get_item_title().text)
#
#    cp.product_confirm()
#
#    """Страница оформления заказа"""
#    """Ввод данных, подтверждение заказа."""
#
#    # cip = Order_page(driver)
#    # cip.input_information()
#
#    """Страница с одобрением заказа"""
#
#    # f = Finish_page(driver)
#    # f.finish()
#
#    time.sleep(3)
#    driver.quit()

#test_buy_product_2()
