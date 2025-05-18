from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Order_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    full_name = "//input[@name='ORDER_PROP_1']"
    pref_connection = "//input[@name='ORDER_PROP_20']"
    phone_number = "//input[@name='ORDER_PROP_3']"
    client_button = "//*[@id='bx-soa-properties']/div[4]/div[3]/div"
    continue_button = "//*[@id='bx-soa-total']/div[2]/div[1]/div[7]/a"


    # Getters

    def get_full_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_name)))

    def get_pref_connection(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pref_connection)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_client_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.client_button)))

    # Actions

    def input_full_name(self, first_name):
        self.get_full_name().send_keys(first_name)
        print("Input First Name")

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print("Input Phone Number")

    def input_pref_connection(self, pref_connection):
        self.get_pref_connection().send_keys(pref_connection)
        print("Input Preferred Connection")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click Continue Button")

    def click_client_button(self):
        self.get_client_button().click()
        print("Click Client Button")

    # Methods

    def input_information(self):
        self.get_current_url()
        self.input_full_name('')
        self.input_phone_number('')
        self.input_pref_connection('Telegram')

        self.click_client_button()
        self.click_continue_button()