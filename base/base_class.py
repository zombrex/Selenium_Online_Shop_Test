import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver

# Method Get Current URL
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url)

# Method Assert word
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good Value Word")

# Method Screenshot
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('../screen/' + name_screenshot)
        print("Screenshot Saved")

# Method Assert URL
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good URL")
