import requests

BACKEND_URL = "http://127.0.0.1:5000/search"

def search_places(query):
    """Send query to Flask backend dan get result"""
    try:
        resp = requests.post(BACKEND_URL, json={"query": query})
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    results = search_places("best cake shop in Jakarta")
    for r in results:
        print(f"{r['name']} - {r['address']}")
        print(f"Maps: {r['maps_url']}")
