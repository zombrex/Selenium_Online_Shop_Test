from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import Base
from pages.main_page import Main_page


class Login_page(Base):

    url = 'https://mixpcshop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    user_name = "//input[@id='USER_LOGIN_POPUP']"
    password = "//input[@id='USER_PASSWORD_POPUP']"
    login_button = "//button[@name='Login1']"
    main_word = "//*[@id='header']/div/div[1]/div/div/div[6]/div/div/div/div/a/span/span"
    link_cabinet = "//*[@id='header']/div/div[1]/div/div/div[6]/div/div/div/div"


    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_link_cabinet(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_cabinet)))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input Username")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login Button")

    def click_link_cabinet(self):
        self.get_link_cabinet().click()
        print("Click Link Cabinet")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.click_link_cabinet()
        self.input_user_name('isupovilya@gmail.com')
        self.input_password('zombrex66')
        self.click_login_button()
        time.sleep(2)
        print(self.get_main_word().text)
        self.assert_word(self.get_main_word(), "МОЙ КАБИНЕТ")
        self.driver.get(self.url)


