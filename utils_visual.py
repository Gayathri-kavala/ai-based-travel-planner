import os
import requests
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def get_ai_image(query):
    try:
        headers = {"Authorization": PEXELS_API_KEY}
        url = f"https://api.pexels.com/v1/search?query={query}&per_page=1"
        response = requests.get(url, headers=headers, timeout=5)
        data = response.json()
        photo_url = data['photos'][0]['src']['medium']
        return photo_url  # Return the image URL instead of the image itself
    except Exception as e:
        print("Image fetch error:", e)
        return None
