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
    finish_text = "//h1[@id='pagetitle']"

    # Getters
    def get_finish_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_text)))

    # Actions

    # Methods

    def finish(self):
        self.get_current_url()
        time.sleep(5)
        self.get_screenshot()
        self.assert_word(self.get_finish_text(), "Заказ сформирован")


