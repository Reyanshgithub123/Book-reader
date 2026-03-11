from scraper.bestseller_scraper import scrape_bestseller_page
from scraper.book_scraper import scrape_book_details
from processing.clean_data import clean_dataset
import pandas as pd
import time


def main():

    print("Scraping bestseller page...")

    books = scrape_bestseller_page()

    print("Total books found:", len(books))

    for book in books:

        print("Processing:", book["title"])

        desc, pub, date = scrape_book_details(book["url"])

        book["description"] = desc
        book["publisher"] = pub
        book["publication_date"] = date

        time.sleep(2)

    df = pd.DataFrame(books)

    df = clean_dataset(df)

    df.to_csv("output/kindle_dataset.csv", index=False)

    print("Dataset saved to output/kindle_dataset.csv")


if __name__ == "__main__":
    main()