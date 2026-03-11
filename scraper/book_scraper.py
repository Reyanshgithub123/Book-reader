import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def scrape_book_details(url):

    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, "lxml")

        description = ""
        publisher = ""
        pub_date = ""

        desc_tag = soup.select_one("#bookDescription_feature_div")

        if desc_tag:
            description = desc_tag.text.strip()

        details = soup.select("#detailBullets_feature_div li")

        for d in details:

            text = d.text.lower()

            if "publisher" in text:
                publisher = d.text.strip()

            if "publication date" in text:
                pub_date = d.text.strip()

        return description, publisher, pub_date

    except:
        return "", "", ""