from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    checkout_button = "//button[@data-entity='basket-checkout-button']"
    item_title = "//h2[@class='basket-item-info-name']//span[1]"
    item_price = "//div[@class='basket-item-price-current-value']"
    total_price = "//div[@class='basket-coupon-block-total-price-current']"


    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))
    def get_item_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_title)))
    def get_item_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_price)))
    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click Checkout Button")


    # Methods
    def assert_price(self):
        item_price = ''.join(c if c.isdigit() else '' for c in self.get_item_price().text)
        total_price = ''.join(c if c.isdigit() else '' for c in self.get_total_price().text)
        assert total_price == item_price
        print(f'Total Price {total_price} is OK')

    def assert_item_title(self,cat_item_title):
        item_cart_title = self.get_item_title().text
        assert item_cart_title == cat_item_title
        print(f'Item Title {cat_item_title} is OK')



    def product_confirm(self,cat_item_title):
        self.get_current_url()
        self.assert_price()
        self.assert_item_title(cat_item_title)
        self.click_checkout_button()
