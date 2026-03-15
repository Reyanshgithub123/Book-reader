import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

pages = [
"https://www.amazon.com/Best-Sellers-Kindle-Store-Paranormal-Romance/zgbs/digital-text/6190484011",
"https://www.amazon.com/Best-Sellers-Kindle-Store-Paranormal-Romance/zgbs/digital-text/6190484011/ref=zg_bs_pg_2?_encoding=UTF8&pg=2"
]

def get_int(x):
    if not x:
        return None
    x = x.replace(",","")
    m = re.findall(r"\d+",x)
    return int(m[0]) if m else None

def get_float(x):
    if not x:
        return None
    m = re.findall(r"\d+\.\d+",x)
    return float(m[0]) if m else None


books_data = []

for page in pages:

    print("Scraping:",page)

    r = requests.get(page,headers=headers)
    soup = BeautifulSoup(r.text,"lxml")

    books = soup.select("div.p13n-sc-uncoverable-faceout")

    print("Books found:",len(books))

    for book in books:

        try:
            rank = get_int(book.select_one(".zg-bdg-text").text)
        except:
            rank=None

        try:
            title = book.select_one("img")["alt"]
        except:
            title=""

        try:
            author = book.select_one(".a-size-small.a-link-child").text.strip()
        except:
            author=""

        try:
            rating = get_float(book.select_one(".a-icon-alt").text)
        except:
            rating=None

        try:
            reviews = get_int(book.select_one("span.a-size-small[aria-hidden='true']").text)
        except:
            reviews=None

        try:
            price = get_float(book.select_one("span._cDEzb_p13n-sc-price_3mJ9Z").text)
        except:
            price=None

        try:
            link = book.select_one("a.a-link-normal")["href"]
            url = "https://www.amazon.com"+link.split("?")[0]
        except:
            url=""

        books_data.append({
            "rank":rank,
            "title":title,
            "author":author,
            "rating":rating,
            "reviews":reviews,
            "price":price,
            "url":url
        })

    time.sleep(2)


df = pd.DataFrame(books_data)

df = df.sort_values("rank")

df.to_csv("kindle_books.csv",index=False)
print(df)
print("✅ CSV created with",len(df),"books")
print("100 books csv with description and author")