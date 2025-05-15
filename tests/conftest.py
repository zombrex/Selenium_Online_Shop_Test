import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

BASE_URL = 'https://mixpcshop.ru/'

@pytest.fixture()
def set_up():
    print("Start Test")

    # Настройки браузера
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())

    # Инициализация драйвера
    driver = webdriver.Chrome(service=service)
    driver.get(BASE_URL)
    driver.maximize_window()

    # Передача драйвера в тест
    yield driver

    # Действия после завершения теста
    time.sleep(3)  # Можно убрать, если не нужно явное ожидание
    driver.quit()

    print("End Test")


