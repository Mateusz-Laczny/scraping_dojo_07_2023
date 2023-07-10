from enum import Enum

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from quotes import Quote


class Webdriver(Enum):
    CHROME = 'chrome'
    FIREFOX = 'firefox'


class SeleniumQuoteScrapper:

    def __init__(self, proxy: str = None, webdriver_to_use=None) -> None:
        if webdriver_to_use is None:
            webdriver_to_use = Webdriver.CHROME
        self.proxy = proxy

        if webdriver_to_use == Webdriver.CHROME:
            options = webdriver.ChromeOptions()
            if proxy is not None:
                options.add_argument(f'--proxy-server={self.proxy}')

            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif webdriver_to_use == Webdriver.FIREFOX:
            options = webdriver.FirefoxOptions()
            if proxy is not None:
                proxy_addr = proxy[:len(proxy) - 5]
                proxy_port = proxy[len(proxy) - 4:]
                options.set_preference('network.proxy.type', 1)
                options.set_preference('network.proxy.socks', proxy_addr)
                options.set_preference('network.proxy.socks_port', proxy_port)
                options.set_preference('network.proxy.socks_remote_dns', False)

            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    def scrape(self, start_url: str) -> list[Quote]:
        self.driver.get(start_url)

        reached_end = False
        quotes_list = []
        while not reached_end:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, "quotesPlaceholder"))
            )
            quotes_html_elements = self.driver.find_elements(By.CLASS_NAME, "quote")
            for quote_html_element in quotes_html_elements:
                author = quote_html_element.find_element(By.CLASS_NAME, "author").text
                quote_text = quote_html_element.find_element(By.CLASS_NAME, "text").text
                tags_html_elements = quote_html_element.find_elements(By.CLASS_NAME, "tag")
                tags = []
                for tags_html_element in tags_html_elements:
                    tags.append(tags_html_element.text)

                quotes_list.append(Quote(by=author, text=quote_text, tags=tags))

            try:
                next_button_element_wrapper = self.driver.find_element(By.CLASS_NAME, "next")
                next_button_element = next_button_element_wrapper.find_element(By.TAG_NAME, "a")
                next_button_element.click()
            except NoSuchElementException:
                reached_end = True

        self.driver.quit()

        return quotes_list
