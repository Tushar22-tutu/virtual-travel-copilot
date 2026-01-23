import random

def search_hotels(data):
    price_per_night = random.randint(1500, 6000)
    rating = round(random.uniform(3.5, 4.8), 1)

    return {
        "type": "hotel",
        "destination": data.get("destination", "Unknown"),
        "price_per_night": price_per_night,
        "rating": rating
    }

