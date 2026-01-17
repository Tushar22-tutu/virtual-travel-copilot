
def search_flights(data):
    return {
        "type": "flight",
        "from": "DEL",
        "to": data.get("destination", "Unknown"),
        "price": 5000
    }
