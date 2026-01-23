
import random

def search_flights(data):
    base_price = random.randint(3000, 9000)

    # thoda destination ke hisaab se variation
    dest = data.get("destination", "").lower()
    if dest in ["goa", "mumbai", "delhi"]:
        base_price += 1000
    elif dest in ["dubai", "singapore"]:
        base_price += 8000

    return {
        "type": "flight",
        "from": "DEL",
        "to": data.get("destination", "Unknown"),
        "price": base_price
    }

