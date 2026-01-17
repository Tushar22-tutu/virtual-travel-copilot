from services.flight_service import search_flights
from services.hotel_service import search_hotels
from itinerary_builder import build_itinerary


def normalize_intent(intent: str):
    intent = intent.lower().strip()

    if "flight" in intent:
        return "flight"
    elif "hotel" in intent:
        return "hotel"
    elif "trip" in intent or "plan" in intent or "package" in intent:
        return "plan trip"
    else:
        return "unknown"


def fix_destination(ai_json: dict):
    # Agar destination empty ho to demo ke liye default set karo
    if not ai_json.get("destination") or ai_json.get("destination") == "":
        ai_json["destination"] = "Goa"
    return ai_json


def decide_action(ai_json: dict):
    # Destination fix
    ai_json = fix_destination(ai_json)

    # Intent normalize
    raw_intent = ai_json.get("intent", "")
    intent = normalize_intent(raw_intent)

    print("RAW INTENT:", raw_intent)
    print("FINAL INTENT:", intent)
    print("DESTINATION:", ai_json.get("destination"))

    # Flight only
    if intent == "flight":
        return search_flights(ai_json)

    # Hotel only
    elif intent == "hotel":
        return search_hotels(ai_json)

    # Full trip
    elif intent == "plan trip":
        flights = search_flights(ai_json)
        hotels = search_hotels(ai_json)

        data = {
            "flights": flights,
            "hotels": hotels
        }

        return build_itinerary(data)

    # Fallback
    else:
        return {
            "error": "Unknown intent",
            "received_intent": raw_intent,
            "ai_json": ai_json
        }

