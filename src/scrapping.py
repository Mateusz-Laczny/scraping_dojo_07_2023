from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from enviroment import proxy

options = Options()
# options.add_argument(f'--proxy-server={proxy}')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("http://quotes.toscrape.com/js-delayed/")
element = WebDriverWait(driver, 20).until(
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
