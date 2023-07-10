import argparse

from environment import input_url, output_file, proxy
from jsonl import write_as_jsonl_file
from selenium_scrapping import SeleniumQuoteScrapper, Webdriver

parser = argparse.ArgumentParser(description="Quotes webscrapper")
parser.add_argument("-b", "--browser", type=str, choices=["chrome", "firefox"], help='Browser to use', default='chrome')
parser.add_argument("-p", "--proxy",action="store_true", help='Flag indicating whether to use proxy')

if __name__ == "__main__":
    args = parser.parse_args()
    webdriver_to_use = Webdriver(args.browser)

    if args.proxy:
        scrapper = SeleniumQuoteScrapper(proxy=proxy, webdriver_to_use=webdriver_to_use)
    else:
        scrapper = SeleniumQuoteScrapper(webdriver_to_use=webdriver_to_use)

    quotes = scrapper.scrape(input_url)
    write_as_jsonl_file(output_file, [quote.as_dict() for quote in quotes])
