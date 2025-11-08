# backend_maps/app.py

from flask import Flask, request, jsonify
import requests
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv  # <- import dotenv

# Load environment variables from file .env in same folder
load_dotenv()

app = Flask(__name__)

# Get API Key from environment variable
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
if not API_KEY:
    raise ValueError("Set GOOGLE_MAPS_API_KEY di .env file!")

# Rate limiter: amx 10 request every minute per IP
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["10 per minute"]
)

# Default location Jakarta
DEFAULT_LOCATION = "-6.200000,106.816666"  # lat,lng
DEFAULT_RADIUS = 5000  # meter

# Cache simple for query
cache = {}

@app.route("/search", methods=["POST"])
@limiter.limit("10 per minute")  # Rate limit per endpoint
def search():
    data = request.json
    query = data.get("query")
    if not query:
        return jsonify({"error": "Query required"}), 400

    # Cek cache
    if query in cache:
        return jsonify(cache[query])

    # location & radius optional from request
    location = data.get("location", DEFAULT_LOCATION)
    radius = data.get("radius", DEFAULT_RADIUS)

    # Call Google Maps Places API
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "location": location,
        "radius": radius,
        "key": API_KEY
    }

    try:
        resp = requests.get(url, params=params, timeout=5).json()
    except requests.RequestException as e:
        return jsonify({"error": "Request to Google Maps failed", "details": str(e)}), 500

    status = resp.get("status")
    if status != "OK":
        return jsonify({
            "error": f"Google Maps API error: {status}",
            "details": resp.get("error_message")
        }), 400

    results = []
    for place in resp.get("results", []):
        results.append({
            "name": place.get("name"),
            "address": place.get("formatted_address"),
            "maps_url": f"https://www.google.com/maps/search/?api=1&query={place.get('name').replace(' ', '+')}"
        })

    # Simpan ke cache
    cache[query] = results

    return jsonify(results)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
