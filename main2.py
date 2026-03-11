import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0"
}

df = pd.read_csv("kindle_books.csv")

descriptions = []
publishers = []
dates = []

for url in df["url"]:

    print("Opening:", url)

    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")

        # ---------- DESCRIPTION ----------
        desc_tag = soup.select_one("#bookDescription_feature_div")

        if desc_tag:
            description = desc_tag.get_text(separator=" ", strip=True)
        else:
            description = "N/A"

        descriptions.append(description)

        # ---------- PUBLISHER + DATE ----------
        publisher = "N/A"
        pub_date = "N/A"

        details = soup.select("li")

        for li in details:

            label = li.select_one(".a-text-bold")

            if label:
                label_text = label.get_text(strip=True)

                value = li.select("span")[-1].get_text(strip=True)

                if "Publisher" in label_text:
                    publisher = value

                if "Publication date" in label_text:
                    pub_date = value

        publishers.append(publisher)
        dates.append(pub_date)

    except Exception as e:
        print("Error:", e)
        descriptions.append("Error")
        publishers.append("Error")
        dates.append("Error")

    time.sleep(3)  # Amazon block avoid

df["description"] = descriptions
df["publisher"] = publishers
df["publication_date"] = dates

df.to_csv("books_details.csv", index=False)

print("✅ books_details.csv created")