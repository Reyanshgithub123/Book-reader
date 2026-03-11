import pandas as pd
from scraper.utils import clean_rating, clean_reviews, clean_price, clean_rank


def clean_dataset(df):

    df["rating"] = df["rating"].apply(clean_rating)

    df["reviews"] = df["reviews"].apply(clean_reviews)

    df["price"] = df["price"].apply(clean_price)

    df["rank"] = df["rank"].apply(clean_rank)

    return df