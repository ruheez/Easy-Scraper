import os
from selenium import webdriver

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRIVERS_PATH = os.path.join(PARENT_DIR, 'drivers')

# Check if current device is windows or linux
if os.name == 'nt':
    DRIVER_PATH = os.path.join(DRIVERS_PATH, 'geckodriver-30.exe')
else:
    DRIVER_PATH = os.path.join(DRIVERS_PATH, 'geckodriver-30')


class Scraper:
    def __init__(self):
        # Make browser headless
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        # Initialize webdriver
        self.driver = webdriver.Firefox(executable_path=DRIVER_PATH, options=options)

    # Get page url
    def get_page(self, url):
        self.driver.get(url)

    # Check if keyword exists in page
    def check_keyword(self, keyword):
        return keyword in self.driver.page_source

    def click_element_xpath(self, xpath):
        self.driver.find_element(xpath).click()

    def get_element_text_xpath(self, xpath):
        return self.driver.find_element(xpath).text

    # Close browser
    def close(self):
        self.driver.close()


if __name__ == '__main__':
    url = 'https://app.parlamento.pt/BI2/'
    scraper = Scraper()
    scraper.get_page(url)
    print(scraper.check_keyword('Cannabis'))
    scraper.close()
