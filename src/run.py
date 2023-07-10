from environment import input_url, output_file
from jsonl import write_as_jsonl_file
from selenium_scrapping import SeleniumQuoteScrapper

if __name__ == '__main__':
    scrapper = SeleniumQuoteScrapper()
    quotes = scrapper.scrape(input_url)
    write_as_jsonl_file(output_file, [quote.as_dict() for quote in quotes])
