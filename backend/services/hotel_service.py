
def search_hotels(data):
    return {
        "type": "hotel",
        "destination": data.get("destination", "Unknown"),
        "price_per_night": 2000,
        "rating": 4.2
    }

