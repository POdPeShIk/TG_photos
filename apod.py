import requests
import os
import argparse
from dotenv import load_dotenv

from save_file import save


def get_links(api_key):
    payload = {"api_key": api_key, "count": 30}
    links = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    return links


def thirty_links(api_key, date = "today"):
    payload={"api_key": api_key,
        "date": date}
    links= get_links(api_key)
    links = links.json()
    counter = 0
    for link in links:
        image_url = link["url"]
        counter += 1
        filename=f"apod_{counter}"
        save(image_url , filename, "APOD",api_key)


if __name__ == "__main__":
    load_dotenv()
    api_key=os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser(
        description='Описание что делает программа'
    )
    parser.add_argument('--date', help='YYYY-MM-DD')
    args = parser.parse_args()
    if args.date:
        date = args.date
        thirty_links(api_key,date)
    else:
        thirty_links(api_key)


