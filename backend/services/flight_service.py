def search_flights(data):
    return {
        "type": "flight",
        "from": "DEL",
        "to": data["destination"],
        "price": 5000
    }
