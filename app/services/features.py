from rapidfuzz import fuzz

KNOWN_BRANDS = [
    "phonepe",
    "paytm",
    "google pay",
    "gpay",
    "bhim"
]

def name_similarity(a, b):
    return fuzz.token_set_ratio(a.lower(), b.lower()) / 100


def detect_brand(app_name):
    name = app_name.lower()
    for brand in KNOWN_BRANDS:
        if brand in name:
            return brand
    return None
