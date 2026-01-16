from services.flight_service import search_flights
from services.hotel_service import search_hotels

def decide_action(ai_json):
    intent = ai_json.get("intent")

    if intent in ["flight", "book flight"]:
        return search_flights(ai_json)

    elif intent in ["hotel", "book hotel"]:
        return search_hotels(ai_json)

    elif intent in ["plan trip", "plan a trip", "package"]:
        flights = search_flights(ai_json)
        hotels = search_hotels(ai_json)
        return {
            "flights": flights,
            "hotels": hotels
        }

    else:
        return {"error": "Unknown intent"}
