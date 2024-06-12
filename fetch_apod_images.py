import requests
import os
from dotenv import load_dotenv

from save_file import save


def get_links(api_key):
    payload = {
        "api_key": api_key,
        "count": 30
    }
    links = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    return links


def get_thirty_links(api_key):
    links = get_links(api_key)
    links = links.json()
    for link_number, link in enumerate(links):
        image_url = link["url"]
        filename = f"apod_{link_number}"
        save(image_url, filename, "APOD", api_key)


if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    get_thirty_links(api_key)
