from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import Base


class Finish_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    # Getters

    # Actions

    # Methods

    def finish(self):
        self.get_current_url()
        time.sleep(5)
# <h1 id="pagetitle">Заказ сформирован</h1>
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')
        self.get_screenshot()
