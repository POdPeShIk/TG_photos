import requests
import os
from dotenv import load_dotenv


from save_file import save


def get_links(api_key):
    payload = {"api_key": api_key, "count": 30}
    links = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    return links


def thirty_links(api_key):
    links= get_links(api_key)
    links = links.json()
    counter = 0
    for link in links:
        image_url = link["url"]
        counter += 1
        filename=f"apod_{counter}"
        save(image_url , filename, "APOD")


if __name__ == "__main__":
    load_dotenv(".env")
    api_key=os.environ['API_KEY']
    thirty_links(api_key)
