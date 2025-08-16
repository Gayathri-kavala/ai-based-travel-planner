import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def generate_itinerary(destination, start_date, end_date):
    prompt = (
        f"Create a detailed day-by-day itinerary for a trip to {destination} "
        f"from {start_date} to {end_date}. Include top attractions, local food spots, and activities. "
        f"Format each day as:\n\nDay X:\n- Morning:\n- Afternoon:\n- Evening:\n"
    )

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "z-ai/glm-4.5-air:free",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
    data = response.json()

    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    else:
        return f"❌ Error: {data.get('error', {}).get('message', 'Unknown error')}"

def get_pexels_image(query):
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    params = {
        "query": query,
        "per_page": 1
    }
    response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        photos = data.get("photos", [])
        if photos:
            return photos[0]["src"]["landscape"]
    return None
