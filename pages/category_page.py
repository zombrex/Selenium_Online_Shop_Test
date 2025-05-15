from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


from base.base_class import Base
import time


class Category_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(driver)



    # Locators
    cart = "//div[@class='wrap_icon inner-table-block top_basket']//i"
    dropdown_filter = "//div[@class='dropdown-select']"
    product_title_1 ="//div[@class='item-title']//span[1]"
    select_move_to_product = "//div[@class='inner_wrap TYPE_1'][1]"
    select_product_1 = "//i[@title='В корзину'][1]"


    # Getters

    def get_dropdown_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_filter )))

    def get_dropdown_filter_items(self,dropdown_filter_item):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, dropdown_filter_item)))

    def get_product_title_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_title_1)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.select_product_1)))

        #return self.driver.find_element(By.XPATH, self.select_product_1)

    def get_move_to_product(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.select_move_to_product)))
        #return self.driver.find_element(By.XPATH, self.select_move_to_product)

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    # Actions
    # Раскрываем Dropdown список фильтров цен, названий по убыванию или возрастанию
    def dropdown_filter_select(self):
        self.get_dropdown_filter().click()
        print("Dropdown Filter Click")


    def dropdown_filter_item_select(self, dropdown_filter_name):
        dropdown_filter_items = f"//div[@class='dropdown-select__list-item font_xs']//span[text()='{dropdown_filter_name}']"
        self.get_dropdown_filter_items(dropdown_filter_items).click()
        print("Dropdown Filter Select")


    # Цепочка действий для наведения на товар и добавления в корзину
    def move_to_product(self):
        STEP_1 = self.driver.find_element(By.XPATH, self.select_move_to_product)
        STEP_2 = self.driver.find_element(By.XPATH, self.select_product_1)
        self.action.move_to_element(STEP_1).move_to_element(STEP_2).perform()
        print("Move To Product")

    def click_select_product_1(self):
        self.action.click(self.get_select_product_1()).perform()
        print("Click Select Product 1")


    def click_cart(self):
        self.action.move_to_element(self.get_cart()).click().perform()
        print("Click Cart")


    # Кликаем для раскрытия фильтра (название фильтра задаётся при вызове функции)
    def click_show_filter(self, filter_name):
        filter_locator = f"//div[@data-property_name='{filter_name}']"
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, filter_locator))).click()
        print(f"Click Show Filter {filter_name}")

    # Кликаем на значение в фильтре (значение задаётся при вызове функции)
    def click_filter(self, filter_name, filter_checkbox):
        filter_checkbox_locator = f"//div[@data-property_name='{filter_name}']//span[@title='{filter_checkbox}']"

        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, filter_checkbox_locator))).click()

        print(f"Click Filter Checkbox {filter_checkbox}")


    # Methods

    def select_products_1(self):
        self.get_current_url()

    # Раскрываем Dropdown список фильтров
        self.dropdown_filter_select()
    # Выбираем Dropdown фильтр
        self.dropdown_filter_item_select('По популярности (убывание)')

    # Раскрываем фильтр из колонки слева и кликаем, выбираем фильтры в функциях
        self.click_show_filter('Сокет')
        self.click_filter('Сокет', 'AM4')

    # Ожидание обновления товаров
        time.sleep(3)

        self.click_show_filter('Количество ядер')
        self.click_filter('Количество ядер', '4')

    # Ожидание обновления товаров
        time.sleep(3)

        cat_product_title = self.get_product_title_1().text

    # Наводим на товар и добавляем в корзину
        self.move_to_product()
        self.click_select_product_1()

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class='notice__text-wrap']"))
        )
        time.sleep(1)
        self.click_cart()

        return cat_product_title

    def select_products_2(self):
        self.get_current_url()

    # Раскрываем Dropdown список фильтров
        self.dropdown_filter_select()
    # Выбираем Dropdown фильтр
        self.dropdown_filter_item_select('По цене (возрастание)')

     # Раскрываем фильтр из колонки слева и кликаем, выбираем фильтры в функциях
        self.click_show_filter('Производитель чипа')
        self.click_filter('Производитель чипа', 'NVIDIA')

        time.sleep(3)

        self.click_show_filter('Объем видеопамяти')
        self.click_filter('Объем видеопамяти', '8GB')

        # Ожидание обновления товаров
        time.sleep(3)

        cat_product_title = self.get_product_title_1().text

        # Наводим на товар и добавляем в корзину
        self.move_to_product()
        self.click_select_product_1()

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class='notice__text-wrap']"))
        )
        time.sleep(1)
        self.click_cart()
        return cat_product_title


    def select_products_3(self):
        self.get_current_url()

    # Раскрываем Dropdown список фильтров
        self.dropdown_filter_select()
    # Выбираем Dropdown фильтр
        self.dropdown_filter_item_select('По цене (возрастание)')


        # Ожидание обновления товаров
        time.sleep(3)

        cat_product_title = self.get_product_title_1().text

        # Наводим на товар и добавляем в корзину
        self.move_to_product()
        self.click_select_product_1()

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class='notice__text-wrap']"))
        )
        time.sleep(1)
        self.click_cart()
        return cat_product_title