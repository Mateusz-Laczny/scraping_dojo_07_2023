from environment import input_url
from selenium_scrapping import SeleniumScrapper

if __name__ == '__main__':
    scrapper = SeleniumScrapper()
    quotes = scrapper.scrape(input_url)
    print(quotes)
