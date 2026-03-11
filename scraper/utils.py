import re

def clean_rating(text):
    if not text:
        return None
    try:
        return float(text.split()[0])
    except:
        return None


def clean_reviews(text):
    if not text:
        return None
    text = text.replace(",", "")
    try:
        return int(text)
    except:
        return None


def clean_price(text):
    if not text:
        return None
    text = text.replace("$", "")
    try:
        return float(text)
    except:
        return None


def clean_rank(text):
    if not text:
        return None
    text = text.replace("#", "")
    try:
        return int(text)
    except:
        return None