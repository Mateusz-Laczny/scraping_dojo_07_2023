from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from environment import input_url

options = Options()
# options.add_argument(f'--proxy-server={proxy}')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get(input_url)

reached_end = False
while not reached_end:
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "quotesPlaceholder"))
    )
    quotes_html_elements = driver.find_elements(By.CLASS_NAME, "quote")
    for quote_html_element in quotes_html_elements:
        quote_text = quote_html_element.find_element(By.CLASS_NAME, "text").text
        author = quote_html_element.find_element(By.CLASS_NAME, "author").text
        tags_html_elements = quote_html_element.find_elements(By.CLASS_NAME, "tag")
        tags = []
        for tags_html_element in tags_html_elements:
            tags.append(tags_html_element.text)

        print('Quote:\n', quote_text, '\nAuthor:\n', author, '\nTags:\n', tags, end='\n')

    try:
        next_button_element_wrapper = driver.find_element(By.CLASS_NAME, "next")
        next_button_element = next_button_element_wrapper.find_element(By.TAG_NAME, "a")
        next_button_element.click()
    except NoSuchElementException:
        reached_end = True
