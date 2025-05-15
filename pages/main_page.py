from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


from base.base_class import Base

class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(driver)


    # Locators
    # Шаблон локатора категории
    category_locator_template = "//div[@class='name font_sm']//a[contains(text(), '{}')]"
    cart = "//div[@class='wrap_icon inner-table-block top_basket']//i"

    # Getters
    def get_category(self, category_name):
        locator = self.category_locator_template.format(category_name)
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, locator)))

    # Actions
    # Кликаем категорию товара
    def click_category(self, category_name):
        self.action.move_to_element(self.get_category(category_name)).click().perform()

        #self.get_category(category_name).click()
        print(f"Click Category: {category_name}")

    # Methods
    # Выбираем категорию товаров
    def choose_category(self, category_name):
        #self.driver.get(self.url)
        self.get_current_url()
        self.click_category(category_name)
