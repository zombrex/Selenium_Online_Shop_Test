import time,pytest

from selenium import webdriver

from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.category_page import Category_page
from pages.cart_page import Cart_page
from pages.order_page import Order_page
from pages.finish_page import Finish_page


# Тест 1 с выбором категории Процессоры
@pytest.mark.cpu
def test_buy_product_1(set_up):
   driver = set_up

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
   cp.product_confirm(cat_product_title)

   """Страница оформления заказа"""
   """Ввод данных, подтверждение заказа."""

   # cip = Order_page(driver)
   # cip.input_information()

   """Страница с одобрением заказа"""

   # f = Finish_page(driver)
   # f.finish()


# Тест 2 с выбором категории Видеокарты
@pytest.mark.videocard
def test_buy_product_2(set_up):
   driver = set_up

   """Авторизация пользователя"""

   #login = Login_page(driver)
   #login.authorization()

   """Главная страница - выбор категории (Процессоры, Видеокарты и тд)"""

   mp = Main_page(driver)
   mp.choose_category('Видеокарты')

   """Страница выбранной категории - каталог товаров"""
   """Выбор товаров"""

   cat_p = Category_page(driver)

   cat_product_title = cat_p.select_products_2()

   """Страница корзины"""
   """Подтверждение выбора товаров"""

   cp = Cart_page(driver)
   cp.product_confirm(cat_product_title)

   """Страница оформления заказа"""
   """Ввод данных, подтверждение заказа."""

   # cip = Order_page(driver)
   # cip.input_information()

   """Страница с одобрением заказа"""

   # f = Finish_page(driver)
   # f.finish()

# Тест 3 с выбором категории Аксессуары

@pytest.mark.aks
def test_buy_product_3(set_up):
   driver = set_up

   """Авторизация пользователя"""

   login = Login_page(driver)
   login.authorization()

   """Главная страница - выбор категории (Процессоры, Видеокарты и тд)"""

   mp = Main_page(driver)
   mp.choose_category('Охлаждение')

   """Страница выбранной категории - каталог товаров"""
   """Выбор товаров"""

   cat_p = Category_page(driver)

   cat_product_title = cat_p.select_products_3()

   """Страница корзины"""
   """Подтверждение выбора товаров"""

   cp = Cart_page(driver)
   cp.product_confirm(cat_product_title)

   """Страница оформления заказа"""
   """Ввод данных, подтверждение заказа."""

   cip = Order_page(driver)
   cip.input_information()

   """Страница с одобрением заказа"""

   f = Finish_page(driver)
   f.finish()


