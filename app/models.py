from datetime import datetime


url_store = {}

def create_url_entry(short_code: str, long_url: str):
    """Create a new entry in the store for a short code."""
    url_store[short_code] = {
        "url": long_url,
        "clicks": 0,
        "created_at": datetime.utcnow()
    }

def increment_clicks(short_code: str):
    """Increase clicks count for given short code."""
    if short_code in url_store:
        url_store[short_code]["clicks"] += 1

def get_url_entry(short_code: str):
    """Return the stored metadata for a short code or None."""
    return url_store.get(short_code)
