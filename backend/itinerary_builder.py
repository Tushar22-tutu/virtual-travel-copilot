def build_itinerary(data):
    flights = data.get("flights", {})
    hotels = data.get("hotels", {})

    total_cost = flights.get("price", 0) + hotels.get("price_per_night", 0) * 3

    return {
        "summary": "Best travel plan generated",
        "flight": flights,
        "hotel": hotels,
        "estimated_total_cost": total_cost
    }
