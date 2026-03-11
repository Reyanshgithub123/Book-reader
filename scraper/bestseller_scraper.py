import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Best-Sellers-Kindle-Store-Paranormal-Romance/zgbs/digital-text/7588788011"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def scrape_bestseller_page():

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "lxml")

    books = soup.select("div.zg-grid-general-faceout")

    results = []

    for book in books:

        rank = book.select_one(".zg-badge-text")
        title = book.select_one("img")
        author = book.select_one(".a-size-small.a-link-child")
        rating = book.select_one(".a-icon-alt")
        reviews = book.select_one(".a-size-small")
        price = book.select_one(".p13n-sc-price")
        link = book.select_one("a")

        book_url = None
        if link:
            book_url = "https://amazon.com" + link["href"]

        results.append({
            "rank": rank.text.strip() if rank else "",
            "title": title["alt"] if title else "",
            "author": author.text.strip() if author else "",
            "rating": rating.text if rating else "",
            "reviews": reviews.text if reviews else "",
            "price": price.text if price else "",
            "url": book_url
        })

    return results